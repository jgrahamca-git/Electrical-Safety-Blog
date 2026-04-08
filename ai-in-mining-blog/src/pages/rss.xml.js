import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';
import sanitizeHtml from 'sanitize-html';
import MarkdownIt from 'markdown-it';

const parser = new MarkdownIt();

export async function GET(context) {
	const topics = await getCollection('safety-topics');
	const incidents = await getCollection('incidents', ({ data }) => {
		return data.draft !== true;
	});
	const news = await getCollection('safety-news');
	
	const allPosts = [...topics, ...incidents, ...news]
		.map(post => {
			if (!post.data.pubDate) console.log(post.id);
			return post;
		});

	const now = new Date();
	const endOfToday = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), 23, 59, 59, 999));

	const filteredPosts = allPosts
		.filter((post) => post.data.pubDate.valueOf() <= endOfToday.valueOf())
		.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: context.site,
		items: filteredPosts.map((post) => {
			const imgSrc = typeof post.data.heroImage === 'object' ? post.data.heroImage.src : post.data.heroImage;
			const fullImgUrl = imgSrc ? `https://safetyblog.eli-intelligence.com${imgSrc.startsWith('/') ? '' : '/'}${imgSrc}` : null;
			
			// Safely strip MDX imports and interactive Quiz tags before compiling
			let cleanBody = post.body || '';
			cleanBody = cleanBody.replace(/^import\s+.*?;$/gm, '');
			cleanBody = cleanBody.replace(/<Quiz[\s\S]*?\/>/g, '');

			// Parse the clean markdown body into HTML for email rendering
			let htmlBody = sanitizeHtml(parser.render(cleanBody));

			// Inject the hero image directly into the HTML format for MailerLite's "Full Content" option
			if (fullImgUrl) {
				htmlBody = `<img src="${fullImgUrl}" alt="Featured Image" width="600" style="display: block; width: 100%; max-width: 600px; height: auto; margin-bottom: 20px; border-radius: 8px;" />\n` + htmlBody;
			}

			return {
				title: post.data.title,
				pubDate: post.data.pubDate,
				description: post.data.description,
				link: `/${post.collection}/${post.id}/`,
				content: htmlBody,
				customData: fullImgUrl ? `<enclosure url="${fullImgUrl}" length="0" type="image/jpeg"/><media:content url="${fullImgUrl}" medium="image" />` : '',
			};
		}),
	});
}

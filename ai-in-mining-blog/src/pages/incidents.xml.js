import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';
import sanitizeHtml from 'sanitize-html';
import MarkdownIt from 'markdown-it';

const parser = new MarkdownIt();

export async function GET(context) {
	const incidents = await getCollection('incidents');
	
	const allPosts = [...incidents]
		.filter((post) => post.data.pubDate.valueOf() <= Date.now())
		.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

	return rss({
		title: `${SITE_TITLE} - Incident Reports`,
		description: 'Latest Incident RCAs and Reports',
		site: context.site,
		items: allPosts.map((post) => {
			const imgSrc = typeof post.data.heroImage === 'object' ? post.data.heroImage.src : post.data.heroImage;
			const fullImgUrl = imgSrc ? `https://safetyblog.eli-intelligence.com${imgSrc.startsWith('/') ? '' : '/'}${imgSrc}` : null;
			
			// Safely strip MDX imports and interactive Quiz tags before compiling
			let cleanBody = post.body || '';
			cleanBody = cleanBody.replace(/^import\s+.*?;$/gm, '');
			cleanBody = cleanBody.replace(/<Quiz[\s\S]*?\/>/g, '');

			// Parse the clean markdown body into HTML for email rendering
			const htmlBody = sanitizeHtml(parser.render(cleanBody));

			return {
				title: post.data.title,
				pubDate: post.data.pubDate,
				description: post.data.description,
				link: `/${post.collection}/${post.id}/`,
				content: htmlBody,
				customData: fullImgUrl ? `<enclosure url="${fullImgUrl}" length="0" type="image/jpeg"/>` : '',
			};
		}),
	});
}

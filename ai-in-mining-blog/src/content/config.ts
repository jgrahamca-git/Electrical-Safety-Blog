import { defineCollection, z } from 'astro:content';

const incidents = defineCollection({
	type: 'content',
	schema: ({ image }) => z.object({
		title: z.string(),
		description: z.string().optional(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: image().optional().or(z.string().optional()),
		hideMeta: z.boolean().optional(),
		hideNewsletter: z.boolean().optional(),
	}),
});

const safetyTopics = defineCollection({
	type: 'content',
	schema: ({ image }) => z.object({
		title: z.string(),
		description: z.string().optional(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: image().optional().or(z.string().optional()),
	}),
});

const safetyNews = defineCollection({
	type: 'content',
	schema: ({ image }) => z.object({
		title: z.string(),
		description: z.string().optional(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: image().optional().or(z.string().optional()),
	}),
});

export const collections = {
	'incidents': incidents,
	'safety-topics': safetyTopics,
	'safety-news': safetyNews,
};

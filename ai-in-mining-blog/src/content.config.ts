import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const postSchema = ({ image }: any) =>
	z.object({
		title: z.string(),
		description: z.string(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		draft: z.boolean().optional(),
		heroImage: z.optional(image()),
	});

const incidents = defineCollection({
	loader: glob({ base: './src/content/incidents', pattern: '**/*.{md,mdx}' }),
	schema: postSchema,
});

const safetyTopics = defineCollection({
	loader: glob({ base: './src/content/safety-topics', pattern: '**/*.{md,mdx}' }),
	schema: postSchema,
});

const safetyNews = defineCollection({
	loader: glob({ base: './src/content/safety-news', pattern: '**/*.{md,mdx}' }),
	schema: postSchema,
});

export const collections = { incidents, 'safety-topics': safetyTopics, 'safety-news': safetyNews };

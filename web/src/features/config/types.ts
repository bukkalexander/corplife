import { z } from 'zod';

export const ConfigSchema = z.object({
  apiUrl: z.string().url(),
  region: z.string(),
  userPoolId: z.string(),
  userPoolWebClientId: z.string(),
});

export type Config = z.infer<typeof ConfigSchema>;

import { z } from 'zod';

export const fetchData = async <T>(url: string, schema: z.ZodType<T>): Promise<T> => {
  console.log(`Fetching data from ${url}...`);
  const response = await fetch(url);
  console.log(`Fetching data from ${url} DONE`);

  if (!response.ok) {
    throw new Error(`Failed to fetch data: ${response.statusText}`);
  }

  const data = await response.json();
  const result = schema.safeParse(data);

  if (!result.success) {
    throw new Error(`Validation error: ${result.error}`);
  }

  return result.data;
};

export const postData = async <T, U>(
  url: string,
  data: T,
  requestSchema: z.ZodType<T>,
  responseSchema: z.ZodType<U>,
): Promise<U> => {
  const requestResult = requestSchema.safeParse(data);
  if (!requestResult.success) {
    throw new Error(`Validation error: ${requestResult.error}`);
  }

  console.log(`Posting data to ${url}...`);
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestResult.data),
  });
  console.log(`Posting data to ${url} DONE`);

  if (!response.ok) {
    throw new Error(`Failed to post data: ${response.statusText}`);
  }

  const responseData = await response.json();
  const responseResult = responseSchema.safeParse(responseData);

  if (!responseResult.success) {
    throw new Error(`Response validation error: ${responseResult.error}`);
  }

  return responseResult.data;
};

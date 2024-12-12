import { z } from 'zod';

export const loadFromLocalStorage = <T>(key: string, schema: z.ZodType<T>): T | null => {
  const item = localStorage.getItem(key);
  if (!item) {
    return null;
  }

  const parsedItem = JSON.parse(item);
  const result = schema.safeParse(parsedItem);
  if (!result.success) {
    throw new Error(`Validation error: ${result.error}`);
  }
  return result.data;
};

export const saveToLocalStorage = <T>(key: string, data: T, schema: z.ZodType<T>): void => {
  const result = schema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation error: ${result.error}`);
  }

  if (data) {
    localStorage.setItem(key, JSON.stringify(result.data));
  } else {
    localStorage.removeItem(key);
  }
};

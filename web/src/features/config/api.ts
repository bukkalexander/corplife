import { CONFIG_URL } from '@/constants';
import { Config, ConfigSchema } from '@features/config/types';
import { fetchData } from '@services/api';

export const fetchConfig = async (): Promise<Config> => {
  return await fetchData<Config>(CONFIG_URL, ConfigSchema);
};

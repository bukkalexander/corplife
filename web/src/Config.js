

const config =  {

   API_URL : import.meta.env.VITE_API_URL || `http://${import.meta.env.VITE_API_HOST}:${import.meta.env.VITE_API_PORT}`
};

export default config;
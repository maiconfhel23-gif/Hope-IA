/vercel-plugin:build-agents
/vercel-plugin:ai-sdk
/vercel-plugin:deploy prod
npx plugins add vercel/vercel-plugin

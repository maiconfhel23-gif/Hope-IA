
// api/auto-evolution.ts
import { NextRequest, NextResponse } from 'next/server';

export const config = { runtime: 'edge' };

export default async function handler(req: NextRequest) {
  try {
    const { action, payload } = await req.json();

    // PILAR 1: Gerador de Algoritmos (Auto-Coder)
    if (action === 'generate_module') {
      const prompt = `Crie um módulo TypeScript completo e auto-contido para: ${payload.description}`;
      // Chama o modelo gratuito Qwen Coder
      const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'qwen/qwen-2.5-coder-32b-instruct:free',
          messages: [{ role: 'user', content: prompt }]
        })
      });
      const data = await response.json();
      return NextResponse.json({ success: true, code: data.choices[0].message.content });
    }

    // PILAR 2 & 3: Sandbox + Self-Healing (Auto-Correção)
    if (action === 'self_heal') {
      const healPrompt = `O código a seguir falhou com o erro: "${payload.error}". Corrija o código tornando-o 100% funcional sem dependências externas pagas.\nCódigo:\n${payload.code}`;
      const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'deepseek/deepseek-r1:free',
          messages: [{ role: 'user', content: healPrompt }]
        })
      });
      const data = await response.json();
      return NextResponse.json({ success: true, fixedCode: data.choices[0].message.content });
    }

    // PILAR 4: Auto-Deploy via Deploy Hook Vercel
    if (action === 'trigger_deploy') {
      const webhookUrl = process.env.VERCEL_DEPLOY_HOOK_URL;
      if (webhookUrl) {
        await fetch(webhookUrl, { method: 'POST' });
        return NextResponse.json({ success: true, message: 'Deploy automático iniciado na Vercel.' });
      }
      return NextResponse.json({ success: false, message: 'Webhook não configurado.' });
    }

    return NextResponse.json({ error: 'Ação não reconhecida' }, { status: 400 });

  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
        }

# Guia de Setup Railway - OdontoInsight

Este guia te ajudará a configurar os ambientes de Staging e Production no Railway.

## 📋 Pré-requisitos

- Conta no Railway (https://railway.app)
- Conta no GitHub
- Repositório OdontoInsight criado e com código enviado

## 🚀 Passo 1: Criar Projeto Staging

### 1.1 Acessar Railway
1. Entre em https://railway.app
2. Clique em "New Project"
3. Selecione "Deploy from GitHub repo"
4. Escolha o repositório `odontoinsight`
5. Dê o nome: `odontoinsight-staging`

### 1.2 Adicionar PostgreSQL
1. No dashboard do projeto, clique em "+ New"
2. Selecione "Database" → "PostgreSQL"
3. O Railway criará automaticamente o banco

### 1.3 Configurar Variáveis de Ambiente
Clique no serviço Web → "Variables" e adicione:

```env
# Environment
DJANGO_ENV=staging
DEBUG=True

# Django
SECRET_KEY=cole-uma-chave-segura-aqui
ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}},.railway.app

# Database (Railway preenche automaticamente)
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}

# APIs (adicione suas chaves)
ANTHROPIC_API_KEY=sua-chave-anthropic
STRIPE_SECRET_KEY=sua-chave-stripe-test

# Email (opcional para staging)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

**Como gerar SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 1.4 Configurar Build
1. Vá em "Settings" do serviço Web
2. Em "Build Command", adicione:
```bash
pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput && python manage.py migrate
```

3. Em "Start Command", adicione:
```bash
cd backend && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

4. Em "Root Directory", deixe: `/`

### 1.5 Deploy
1. Clique em "Deploy"
2. Aguarde o build (pode levar 3-5 minutos)
3. Acesse a URL fornecida (algo como: `odontoinsight-staging.up.railway.app`)

---

## 🌟 Passo 2: Criar Projeto Production

### 2.1 Criar Novo Projeto
1. No Railway, clique em "New Project"
2. Novamente "Deploy from GitHub repo"
3. Escolha o repositório `odontoinsight`
4. Dê o nome: `odontoinsight-production`
5. **IMPORTANTE:** Configure o auto-deploy pela branch `main`

### 2.2 Adicionar PostgreSQL
1. Repita o processo: "+ New" → "Database" → "PostgreSQL"

### 2.3 Configurar Variáveis de Ambiente (Production)
⚠️ **ATENÇÃO:** Production usa configurações diferentes!

```env
# Environment
DJANGO_ENV=production
DEBUG=False

# Django
SECRET_KEY=cole-uma-chave-DIFERENTE-e-segura-aqui
ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}},.railway.app

# Database
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}

# APIs (use chaves de PRODUÇÃO)
ANTHROPIC_API_KEY=sua-chave-anthropic-PRODUCAO
STRIPE_SECRET_KEY=sua-chave-stripe-PRODUCAO
STRIPE_WEBHOOK_SECRET=sua-chave-webhook-stripe

# Email (configure provedor real)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@dominio.com
EMAIL_HOST_PASSWORD=sua-senha-app

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 2.4 Configurar Build (Production)
Mesmo processo do staging:

**Build Command:**
```bash
pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**
```bash
cd backend && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 4
```

### 2.5 Deploy Production
1. Deploy
2. Aguarde build
3. Teste a URL

---

## 🔧 Passo 3: Criar Superusuário

Para ambos os ambientes (staging e production), você precisa criar um superusuário.

### Opção 1: Via Railway CLI (Recomendado)

1. Instale o Railway CLI:
```bash
# macOS/Linux
brew install railway

# Windows
npm install -g @railway/cli
```

2. Faça login:
```bash
railway login
```

3. Conecte ao projeto staging:
```bash
railway link odontoinsight-staging
```

4. Execute comando para criar superusuário:
```bash
railway run python backend/manage.py createsuperuser
```

5. Repita para production:
```bash
railway link odontoinsight-production
railway run python backend/manage.py createsuperuser
```

### Opção 2: Via Interface do Railway

1. Vá para o projeto no Railway
2. Clique no serviço "Web"
3. Vá em "Deployments" → última deployment bem-sucedida
4. Clique nos 3 pontinhos → "View Logs"
5. No canto superior direito, clique em "Shell"
6. Execute:
```bash
cd backend && python manage.py createsuperuser
```

---

## 🌐 Passo 4: Configurar Domínio Customizado (Opcional)

### Para Production:

1. No projeto production, clique no serviço Web
2. Vá em "Settings" → "Domains"
3. Clique em "Add Domain"
4. Digite: `odontoinsight.com.br` (ou seu domínio)
5. Copie os registros DNS fornecidos
6. No seu provedor de domínio (Registro.br, GoDaddy, etc):
   - Adicione registro CNAME conforme instruções
7. Aguarde propagação (pode levar até 48h)

### Para Staging:

Use o domínio padrão do Railway: `*.up.railway.app`

---

## 📊 Passo 5: Monitoramento

### Logs em Tempo Real
1. Projeto → Serviço Web → "Deployments"
2. Clique na última deployment
3. "View Logs" para ver logs em tempo real

### Métricas
1. Serviço Web → "Metrics"
2. Veja: CPU, RAM, Requests, Response Time

### Alertas (recomendado)
1. Configure alertas de erro via Railway
2. Integre com Slack ou Discord para notificações

---

## 🔄 Passo 6: CI/CD Automático

O Railway já faz deploy automático quando você faz push:

### Staging (auto-deploy de branch `staging`):
```bash
git checkout staging
git add .
git commit -m "feat: nova funcionalidade"
git push origin staging
# Railway faz deploy automático
```

### Production (auto-deploy de branch `main`):
```bash
git checkout main
git merge staging  # Ou faça um PR no GitHub
git push origin main
# Railway faz deploy automático
```

**Recomendação de Workflow:**
1. Trabalhe e publique direto na branch `staging`
2. Teste no Railway staging
3. Se OK, faça merge de `staging` para `main`
4. O Railway de production publica a branch `main`

---

## ⚡ Passo 7: Configurar Celery + Redis (Opcional - Futuro)

Para tasks assíncronas (WhatsApp, análises pesadas):

### 7.1 Adicionar Redis
1. No projeto Railway: "+ New" → "Database" → "Redis"

### 7.2 Adicionar Worker Service
1. "+ New" → "Empty Service"
2. Nomeie: `celery-worker`
3. Configure mesmo repositório
4. Start Command:
```bash
cd backend && celery -A config worker --loglevel=info
```

### 7.3 Adicionar Beat Service (para tarefas agendadas)
1. "+ New" → "Empty Service"
2. Nomeie: `celery-beat`
3. Start Command:
```bash
cd backend && celery -A config beat --loglevel=info
```

### 7.4 Variáveis de Ambiente
Adicione em todos os serviços (web, worker, beat):
```env
REDIS_URL=${{Redis.REDIS_URL}}
```

---

## 🎯 Checklist Final

### Staging:
- [ ] PostgreSQL criado
- [ ] Variáveis de ambiente configuradas
- [ ] Build bem-sucedido
- [ ] Site acessível na URL do Railway
- [ ] Superusuário criado
- [ ] Admin funciona (`/admin`)
- [ ] Logs sem erros críticos

### Production:
- [ ] PostgreSQL criado
- [ ] Variáveis de ambiente (PRODUCTION) configuradas
- [ ] `DEBUG=False` confirmado
- [ ] Build bem-sucedido
- [ ] Site acessível
- [ ] Superusuário criado
- [ ] Domínio customizado (se aplicável)
- [ ] SSL ativo (HTTPS)
- [ ] Logs sem erros

---

## 🆘 Troubleshooting Comum

### Erro: "Bad Request (400)"
**Causa:** `ALLOWED_HOSTS` não configurado corretamente

**Solução:**
```env
ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}},.railway.app,localhost
```

### Erro: "Static files not found"
**Causa:** Collectstatic não rodou

**Solução:**
Adicione ao Build Command:
```bash
python manage.py collectstatic --noinput
```

### Erro: "Database connection failed"
**Causa:** `DATABASE_URL` não configurada

**Solução:**
Verifique se a variável está assim:
```env
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

### Erro: "ModuleNotFoundError"
**Causa:** Dependência faltando no requirements.txt

**Solução:**
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "fix: atualiza requirements"
git push
```

---

## 📱 URLs Finais

Após configuração:

- **Staging:** `https://odontoinsight-staging.up.railway.app`
- **Production:** `https://odontoinsight.com.br` (seu domínio)
- **Admin Staging:** `https://odontoinsight-staging.up.railway.app/admin`
- **Admin Production:** `https://odontoinsight.com.br/admin`

---

## 💡 Próximos Passos

1. ✅ Ambientes configurados
2. ✅ Deploy automático funcionando
3. 🔜 Implementar modelos de dados (Clinics, Procedures, etc)
4. 🔜 Criar dashboards
5. 🔜 Integrar IA (Anthropic Claude)
6. 🔜 Implementar pagamentos (Stripe)
7. 🔜 Adicionar Celery + Redis
8. 🔜 WhatsApp integration

---

**Dúvidas?** Entre em contato ou consulte:
- Railway Docs: https://docs.railway.app
- Django Docs: https://docs.djangoproject.com

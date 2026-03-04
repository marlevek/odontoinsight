# 🎯 Próximos Passos - OdontoInsight

Guia completo do que fazer AGORA para colocar o projeto no ar.

## ✅ O que já está pronto

1. ✅ Estrutura completa do Django
2. ✅ Apps criadas (core, clinics, procedures, analytics, etc)
3. ✅ Templates básicos (home, dashboard)
4. ✅ Configuração multi-ambiente (local, staging, production)
5. ✅ Arquivos de configuração do Railway
6. ✅ Git inicializado
7. ✅ Documentação completa

## 📋 O que VOCÊ precisa fazer agora

### PASSO 1: Criar Repositório no GitHub (5 min)

1. Acesse: https://github.com/new
2. Nome do repositório: `odontoinsight`
3. Deixe **PRIVADO** (é um projeto comercial)
4. **NÃO** adicione README, .gitignore ou licença (já temos)
5. Clique em "Create repository"

6. Copie a URL do repositório (algo como: `https://github.com/SEU-USUARIO/odontoinsight.git`)

7. No seu terminal LOCAL (na máquina onde você vai desenvolver):

```bash
# Baixe os arquivos que eu criei
# (você precisa copiar tudo de /home/claude/odontoinsight para sua máquina)

# Depois, na pasta do projeto:
cd odontoinsight

# Conecte ao GitHub (substitua pela SUA URL)
git remote add origin https://github.com/SEU-USUARIO/odontoinsight.git

# Envie o código
git push -u origin main

# Crie branch staging
git checkout -b staging
git push -u origin staging

# Volte para main
git checkout main
```

---

### PASSO 2: Configurar PostgreSQL Local (10 min)

Se você ainda não tem PostgreSQL 17 instalado:

**Windows:**
1. Baixe: https://www.postgresql.org/download/windows/
2. Instale com senha: `postgres` (ou outra que lembrar)

**Mac:**
```bash
brew install postgresql@17
brew services start postgresql@17
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install postgresql-17
sudo systemctl start postgresql
```

**Criar banco:**
```bash
# Entre no PostgreSQL
psql -U postgres

# Crie o banco
CREATE DATABASE odontoinsight;
CREATE USER odontouser WITH PASSWORD 'odontopass123';
GRANT ALL PRIVILEGES ON DATABASE odontoinsight TO odontouser;
\q
```

---

### PASSO 3: Setup Local (15 min)

```bash
cd odontoinsight

# Crie ambiente virtual
python -m venv venv

# Ative (escolha seu OS):
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Copie o template de .env
cp .env.example .env.local

# EDITE .env.local com seus dados:
# - Adicione SECRET_KEY (gere com o comando abaixo)
# - Configure DB_PASSWORD com a senha que você criou
# - Deixe o resto como está por enquanto
```

**Gerar SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie o resultado e cole no `.env.local` na linha `SECRET_KEY=`

**Rodar o projeto:**
```bash
cd backend

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Digite: username (ex: admin), email, senha

# Coletar static files
python manage.py collectstatic --noinput

# RODAR!
python manage.py runserver
```

**Teste:** http://localhost:8000

Se aparecer a tela inicial do OdontoInsight, **SUCESSO!** ✅

---

### PASSO 4: Configurar Railway - Staging (20 min)

Siga o guia completo em: `docs/RAILWAY_SETUP.md`

**Resumo rápido:**

1. Acesse https://railway.app
2. "New Project" → "Deploy from GitHub repo"
3. Escolha `odontoinsight`
4. Nome: `odontoinsight-staging`
5. Adicione PostgreSQL: "+ New" → "Database" → "PostgreSQL"
6. Configure variáveis de ambiente (veja docs/RAILWAY_SETUP.md)
7. Deploy!

**URLs importantes:**
- Dashboard Railway: https://railway.app/dashboard
- Seu app (após deploy): `https://odontoinsight-staging.up.railway.app`

---

### PASSO 5: Configurar Railway - Production (20 min)

Repita o processo do staging, mas:
- Nome: `odontoinsight-production`
- Use branch `main` (não `staging`)
- **DEBUG=False**
- **SECRET_KEY diferente**
- Use chaves de PRODUÇÃO (Stripe, etc)

---

### PASSO 6: Criar Branches de Trabalho

```bash
# Estrutura de branches recomendada:

# main = produção (recebe apenas código validado)
# staging = homologação (branch de trabalho e testes)

# Exemplo de workflow:
git checkout staging

# ... faça suas alterações ...

git add .
git commit -m "feat: adiciona modelo Clinic"
git push origin staging

# Depois de validar no Railway staging:
git checkout main
git merge staging
git push origin main
# Fluxo atual confirmado: staging -> main
```

---

## 🎨 Próximas Funcionalidades (em ordem)

### Semana 1: Modelos de Dados
```
[ ] Criar modelo Clinic (consultório)
[ ] Criar modelo Dentist (dentista)
[ ] Criar modelo Patient (paciente)
[ ] Criar modelo Procedure (procedimento)
[ ] Criar modelo Material (material)
[ ] Criar modelo Appointment (agendamento)
[ ] Criar modelo Transaction (transação financeira)
```

### Semana 2: CRUD Básico
```
[ ] Interface admin para todos os modelos
[ ] Formulários de cadastro
[ ] Listagens
[ ] Edição e exclusão
```

### Semana 3: Dashboard Financeiro
```
[ ] Gráficos de receita x despesa
[ ] Cards de métricas
[ ] Tabela de procedimentos por lucratividade
[ ] Alertas de horários ociosos
```

### Semana 4: IA - Fase 1
```
[ ] Integração com Anthropic Claude API
[ ] Análise de desperdício de materiais
[ ] Previsão de déficit mensal
[ ] Detecção de risco de churn
```

---

## 📁 Arquivos Importantes

### Para você editar agora:
- `.env.local` - Suas credenciais locais
- `README.md` - Adicione seu nome/GitHub

### Não mexa (por enquanto):
- `backend/config/settings.py` - Configurações Django
- `railway.toml` - Config do Railway
- Arquivos em `backend/apps/` - Apps do projeto

### Próximos a criar:
- `backend/apps/clinics/models.py` - Modelos de consultórios
- `backend/apps/procedures/models.py` - Modelos de procedimentos
- Templates customizados
- Views de CRUD

---

## 🆘 Se Algo Der Errado

### Não consigo instalar dependências
```bash
# Atualize pip
python -m pip install --upgrade pip

# Tente novamente
pip install -r requirements.txt

# Se erro específico, instale um por um:
pip install Django==5.1.5
pip install psycopg2-binary==2.9.10
# etc
```

### Erro de PostgreSQL
```bash
# Verifique se está rodando:
# Windows: Services → PostgreSQL
# Mac: brew services list
# Linux: systemctl status postgresql

# Teste conexão:
psql -U postgres -d odontoinsight
```

### Erro no Railway
- Veja logs: Railway → Seu projeto → Deployments → View Logs
- 90% dos erros são variáveis de ambiente erradas
- Confira `ALLOWED_HOSTS` e `DATABASE_URL`

---

## 💬 Perguntas Frequentes

**Q: Preciso pagar Railway?**
A: Não, o plano free é suficiente no início. Você ganha $5 de crédito grátis por mês.

**Q: Preciso API do Anthropic agora?**
A: Não, deixe em branco por enquanto. Usaremos quando implementarmos a IA.

**Q: Posso mudar de PostgreSQL para outro banco?**
A: Pode, mas PostgreSQL é recomendado (suporta JSONField, melhor performance).

**Q: Quanto tempo leva tudo isso?**
A: Setup inicial: 1-2 horas. Desenvolvimento das funcionalidades: 4-6 semanas.

---

## ✉️ Comandos Git Úteis

```bash
# Ver status
git status

# Adicionar arquivos
git add .
git add arquivo.py

# Commit
git commit -m "tipo: descrição"
# Tipos: feat, fix, docs, style, refactor, test, chore

# Push
git push

# Pull (atualizar)
git pull

# Ver branches
git branch

# Trocar branch
git checkout nome-branch

# Criar nova branch
git checkout -b nova-branch

# Merge
git merge outra-branch

# Ver histórico
git log --oneline

# Desfazer último commit (mantém alterações)
git reset --soft HEAD~1

# Desfazer alterações de arquivo
git checkout -- arquivo.py
```

---

## 🎯 Checklist Imediato

Faça HOJE:

- [ ] Criar repositório GitHub
- [ ] Push do código
- [ ] Instalar PostgreSQL local
- [ ] Criar banco `odontoinsight`
- [ ] Copiar `.env.example` → `.env.local`
- [ ] Gerar e adicionar SECRET_KEY
- [ ] Rodar `python manage.py migrate`
- [ ] Criar superusuário
- [ ] Testar em http://localhost:8000
- [ ] Criar conta Railway (se não tiver)
- [ ] Configurar staging no Railway
- [ ] Testar staging: `https://seu-app.railway.app`

---

**Está pronto! Vamos começar a desenvolver!** 🚀

Qualquer dúvida:
1. Consulte `docs/LOCAL_SETUP.md`
2. Consulte `docs/RAILWAY_SETUP.md`
3. Pesquise no Google: "Django [seu erro]"
4. Pergunte ao Claude! 😉

---

## 📞 Próxima Conversa Comigo

Na próxima vez que conversarmos, podemos:
1. Criar os modelos de dados (Clinic, Patient, Procedure)
2. Implementar o CRUD
3. Melhorar o dashboard
4. Começar a IA preditiva

**IMPORTANTE:** Antes da próxima conversa, complete o setup acima e me diga:
- ✅ Projeto rodando localmente?
- ✅ Staging no Railway funcionando?
- ✅ Algum erro que precisamos resolver?

Aí continuamos juntos! 🤝

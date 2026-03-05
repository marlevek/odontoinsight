# Setup Local - OdontoInsight

Guia passo a passo para rodar o projeto localmente.

## 📋 Pré-requisitos

- Python 3.13+
- PostgreSQL 17
- Git
- virtualenv ou venv

## 🚀 Passo 1: Clone o Repositório

```bash
git clone https://github.com/seu-usuario/odontoinsight.git
cd odontoinsight
```

## 🐍 Passo 2: Criar Ambiente Virtual

### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

## 📦 Passo 3: Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🗄️ Passo 4: Configurar PostgreSQL

### 4.1 Criar Banco de Dados

```bash
# Abra o PostgreSQL
psql -U postgres

# Dentro do psql:
CREATE DATABASE odontoinsight;
CREATE USER odontouser WITH PASSWORD 'suasenha123';
ALTER ROLE odontouser SET client_encoding TO 'utf8';
ALTER ROLE odontouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE odontouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE odontoinsight TO odontouser;
\q
```

### 4.2 Criar Arquivo .env.local

```bash
# Na raiz do projeto
cp .env.example .env.local
```

Edite `.env.local`:

```env
# Environment
DJANGO_ENV=local
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Django
SECRET_KEY=cole-generate-new-secret-key

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=odontoinsight
DB_USER=odontouser
DB_PASSWORD=suasenha123
DB_HOST=localhost
DB_PORT=5432

# APIs (opcional no início)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=

# Email (console para testes)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Redis (se tiver instalado)
REDIS_URL=redis://localhost:6379/0
```

**Gerar SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🔧 Passo 5: Configurar Django

```bash
cd backend

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Digite: username, email, password

# Coletar arquivos estáticos
python manage.py collectstatic --noinput
```

## ▶️ Passo 6: Rodar o Servidor

```bash
# Ainda no diretório backend/
python manage.py runserver
```

Acesse: **http://localhost:8000**

### URLs Importantes:
- Home: http://localhost:8000
- Admin: http://localhost:8000/admin
- Dashboard: http://localhost:8000/dashboard

## 🧪 Passo 7: Testar

```bash
# Rodar testes (quando tivermos)
python manage.py test

# Verificar problemas
python manage.py check
```

## 🔄 Passo 8: Celery (Opcional - para tasks assíncronas)

### 8.1 Instalar Redis (se ainda não tiver)

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install redis-server
sudo systemctl start redis
```

**Mac:**
```bash
brew install redis
brew services start redis
```

**Windows:**
Baixe de: https://github.com/microsoftarchive/redis/releases

### 8.2 Rodar Celery

Terminal 1 - Django:
```bash
cd backend
python manage.py runserver
```

Terminal 2 - Celery Worker:
```bash
cd backend
celery -A config worker --loglevel=info
```

Terminal 3 - Celery Beat (tarefas agendadas):
```bash
cd backend
celery -A config beat --loglevel=info
```

## 📁 Estrutura de Diretórios

```
odontoinsight/
├── backend/
│   ├── apps/
│   │   ├── core/          # Views principais, dashboard
│   │   ├── clinics/       # Gestão de consultórios
│   │   ├── procedures/    # Procedimentos e materiais
│   │   ├── analytics/     # IA e análises
│   │   ├── benchmarking/  # Comparações
│   │   ├── automation/    # WhatsApp, recuperação
│   │   └── reports/       # Relatórios contábeis
│   ├── config/            # Settings Django
│   ├── templates/         # Templates HTML
│   ├── static/            # CSS, JS, images
│   ├── media/             # Uploads
│   └── manage.py
├── docs/                  # Documentação
├── .env.local            # Variáveis locais (não commitado)
├── .env.example          # Template de .env
├── requirements.txt       # Dependências Python
└── README.md
```

## 🛠️ Comandos Úteis

### Django
```bash
# Criar nova app
python manage.py startapp nome_da_app

# Shell interativo
python manage.py shell

# Criar migração específica
python manage.py makemigrations app_name

# Ver SQL de migração
python manage.py sqlmigrate app_name migration_number

# Resetar banco (CUIDADO!)
python manage.py flush

# Carregar dados de fixture
python manage.py loaddata fixture.json

# Criar fixture
python manage.py dumpdata app_name > fixture.json
```

### Git
```bash
# Ver status
git status

# Adicionar arquivos
git add .

# Commit
git commit -m "feat: descrição"

# Push
git push origin branch-name

# Criar nova branch
git checkout -b feature/nome-feature

# Trocar de branch
git checkout branch-name

# Merge
git merge branch-name
```

### PostgreSQL
```bash
# Conectar ao banco
psql -U odontouser -d odontoinsight

# Listar tabelas
\dt

# Descrever tabela
\d nome_tabela

# Ver dados
SELECT * FROM nome_tabela;

# Sair
\q

# Backup
pg_dump -U odontouser odontoinsight > backup.sql

# Restore
psql -U odontouser odontoinsight < backup.sql
```

## 🐛 Troubleshooting

### Erro: "No module named 'apps'"
**Solução:** Verifique se está no diretório `backend/` ao rodar comandos

### Erro: "PostgreSQL connection refused"
**Solução:** 
```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql  # Linux
brew services list  # Mac

# Iniciar se necessário
sudo systemctl start postgresql  # Linux
brew services start postgresql  # Mac
```

### Erro: "ModuleNotFoundError: No module named 'X'"
**Solução:**
```bash
pip install nome-do-modulo
# ou
pip install -r requirements.txt
```

### Erro: "django.core.exceptions.ImproperlyConfigured"
**Solução:** Verifique o arquivo `.env.local` e certifique-se que todas as variáveis estão corretas

### Erro: "CSRF verification failed"
**Solução:** Limpe cookies do navegador ou use aba anônima

## 📊 Variáveis de Ambiente Importantes

```env
# Ambiente
DJANGO_ENV=local|staging|production

# Debug (True só em dev)
DEBUG=True|False

# Hosts permitidos
ALLOWED_HOSTS=localhost,127.0.0.1,dominio.com

# Banco de dados
DATABASE_URL=postgresql://user:pass@host:port/db
# ou
DB_NAME=nome
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

## 🎯 Próximos Passos

1. ✅ Ambiente local configurado
2. 🔜 Criar modelos de dados (Clinic, Dentist, Procedure)
3. 🔜 Implementar CRUD básico
4. 🔜 Criar dashboards
5. 🔜 Integrar IA
6. 🔜 Testes
7. 🔜 Deploy no Railway

---

**Pronto para desenvolver!** 🚀

Qualquer dúvida, consulte a documentação ou peça ajuda.

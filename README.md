# OdontoInsight - CFO Virtual para Consultórios Odontológicos

Sistema inteligente de gestão financeira para consultórios odontológicos, com IA para análise preditiva, benchmarking e automação.

## 🚀 Funcionalidades Principais

### ✅ Fase 1 - Core (Em Desenvolvimento)
- Dashboard financeiro com análise de perdas
- Cadastro de consultórios, dentistas e procedimentos
- Gestão de pacientes e agendamentos

### 🎯 Roadmap

#### Fase 2 - IA Preditiva
- Previsão de déficit mensal
- Análise de risco de churn de pacientes
- Detecção de desperdício de materiais
- Identificação de procedimentos com baixa margem

#### Fase 3 - Benchmarking Anônimo
- Comparação com consultórios similares
- Métricas de performance por especialidade
- Sugestões de otimização baseadas em dados do mercado

#### Fase 4 - Automação de Recuperação
- WhatsApp automatizado para pacientes inativos
- Sugestões de ações para recuperar receita
- Alertas inteligentes de oportunidades

#### Fase 5 - Relatórios Contábeis
- Exportação formatada para contadores
- Relatórios DRE automatizados
- Compliance fiscal simplificado

## 🛠️ Stack Tecnológica

- **Backend:** Django 5.1 + PostgreSQL 17
- **Frontend:** Django Templates + Bootstrap 5
- **IA:** Claude API (Anthropic) + scikit-learn
- **Deploy:** Railway (Staging + Production)
- **Pagamentos:** Stripe (recorrência)

## 📦 Ambientes

- **Local:** Desenvolvimento com PostgreSQL local
- **Staging:** `odontoinsight-staging.railway.app`
- **Production:** `odontoinsight.com.br` (futuro)

## 🔧 Setup Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/odontoinsight.git
cd odontoinsight

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env.local
# Edite .env.local com suas credenciais

# Rode migrações
cd backend
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

Acesse: http://localhost:8000

## 📊 Estrutura do Projeto

```
odontoinsight/
├── backend/
│   ├── config/              # Configurações Django
│   ├── apps/
│   │   ├── core/           # Modelos base e utilitários
│   │   ├── clinics/        # Gestão de consultórios
│   │   ├── procedures/     # Procedimentos e materiais
│   │   ├── analytics/      # IA e análises preditivas
│   │   ├── benchmarking/   # Comparações de mercado
│   │   ├── automation/     # Automações e recuperação
│   │   └── reports/        # Relatórios contábeis
│   ├── templates/          # Templates Django
│   └── static/             # CSS, JS, imagens
├── docs/                   # Documentação
└── requirements.txt        # Dependências Python
```

## 🔐 Variáveis de Ambiente

Crie arquivos `.env.local`, `.env.staging` e `.env.production` baseados em `.env.example`

## 🚢 Deploy Railway

### Staging
```bash
railway link odontoinsight-staging
railway up
```

### Production
```bash
railway link odontoinsight-production
railway up
```

## 📝 Licença

Proprietary - Todos os direitos reservados

## 👥 Autor

Marcelo Zagonel Levek - [@](https://github.com/marlevek)

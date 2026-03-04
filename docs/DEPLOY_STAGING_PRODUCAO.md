# Deploy em Staging e Produção

Este arquivo passa a ser a referência principal para o fluxo de deploy com dois ambientes.

## Estrutura recomendada

- Branch `staging`: homologação
- Branch `main`: produção
- Não usar `develop` como branch permanente

## Fluxo no GitHub

Trabalhe e publique na `staging`:

```bash
git checkout staging
git add .
git commit -m "feat: sua alteração"
git push origin staging
```

Depois de validar no ambiente de staging:

```bash
git checkout main
git merge staging
git push origin main
```

## Staging no Railway

Use o serviço atual como staging.

Configure:

```env
DJANGO_ENV=staging
DEBUG=True
```

Ajustes manuais no painel:

1. Renomear o projeto/serviço para `odontoinsight-staging`
2. Configurar auto-deploy pela branch `staging`
3. Gerar um novo domínio público se quiser remover `production` da URL atual

## Producao no Railway

Crie um segundo projeto/serviço para produção.

Configure:

```env
DJANGO_ENV=production
DEBUG=False
```

Ajustes manuais no painel:

1. Conectar ao mesmo repositorio `odontoinsight`
2. Configurar auto-deploy pela branch `main`
3. Manter banco e variáveis separados de staging

## Variaveis de ambiente

Use [`.env.example`](/d:/Projetos_codertec/odontoinsight/.env.example) como base para:

- `.env.local`
- `.env.staging`
- `.env.production`

Nunca reutilize segredos entre staging e produção.

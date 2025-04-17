## 🔧 Requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.12+
- pip (gerenciador de pacotes Python)
- Virtualenv (opcional, mas recomendado)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone (repositório)
```

### 2. Crie e ative o ambiente virtual

```bash
python3.12 -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 🧪 Executando localmente

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 📁 Estrutura do Projeto

```
aplicação/
├── apps/
│   └── page/             # App principal da aplicação
├── banco/                # Configuração ou dados do banco
├── conf/                 # Arquivos de configuração do projeto
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── templates/            # Templates HTML
├── manage.py             # Entry point do Django
└── requirements.txt      # Lista de dependências Python
```

---

## ✅ Comandos úteis

- Rodar servidor: `python manage.py runserver`
- Coletar arquivos estáticos: `python manage.py collectstatic` ## Se necessário.


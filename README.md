
# 🚀 Como iniciar o projeto

Este projeto utiliza um ambiente virtual (`venv`) para isolar as dependências do Python.

---

## ✅ Requisitos

- Python 3.1 ou superior
- `pip` instalado (geralmente já vem com o Python)

---

## 📦 Criar e ativar o ambiente virtual

### Linux / macOS

```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate
```

### Windows (CMD)

```cmd
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

## 📥 Instalar as dependências

Se o projeto tiver um `requirements.txt`, instale os pacotes com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Rodar o projeto

Você pode agora executar seu script Python normalmente. Exemplo:

```bash
python process_data.py
```

---

## ❌ Desativar o ambiente virtual

Para sair do ambiente virtual:

```bash
deactivate
```

---

## 📚 Referência

* [Documentação oficial do venv (Python)](https://docs.python.org/3/library/venv.html)

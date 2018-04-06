## envio-de-notas

Script criado para monitoria de Matemática Discreta do Centro de Informática (CIn - UFPE)

### Objetivo
Enviar para o email de cada aluno sua nota 

### Bibliotecas
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) - para leitura de arquivos excel
* [Smtplib](https://docs.python.org/3/library/smtplib.html) - para envio de emails

#### Servidores de Email 
para ```smtplib.SMTP_SSL(servidor, porta)```

email     | servidor            |autenticação |porta |
----------|---------------------|-------------|------|
Gmail     | smtp.gmail.com      |      SSL    |  465 |
Hotmail   | smtp.live.com       |       SSL   |  465 |
Outlook   | smtp.live.com       | StartTLS    |  587 |
Yahoo Mail| smtp.mail.yahoo.com |       SSL   |  465 |


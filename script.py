import smtplib
import openpyxl
from openpyxl import load_workbook

#leitura de arquivos
arq = load_workbook(filename = 'arquivo.xlsx', read_only = True)
planilha = arq['sheet name']

#logando no servidor do gmail
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('email', 'senha')

#remetente
de = 'email'

#visitando todos os alunos da planilha
for linhas in planilha.rows:
	login = linhas[coluna_logins].value #pegando logins
	nota = linhas[coluna_notas].value #pegando notas
	
	para = login + "@cin.ufpe.br" #descobrindo email
  
	#debug
	print("de = " + de)
	print("para = " + para)
	print("nota = %d" % nota)
  
	msg = '\r\n'.join([
	'From: %s' % de,
	'To: %s' % para,
	'Subject: (assunto do email) Ex: Notas',
	'',
	'(corpo do email) Ex: A sua nota na prova foi %d' % nota])
  
	#debug
	print("msg = " + msg)
	print()

	#enviando email
	smtp.sendmail(de, para, msg)

#deslogando
smtp.quit()

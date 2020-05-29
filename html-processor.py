import re

def repl(m):  #antikatastash twn html entities me ta antistixa sumbola (xrhsh synarthshs)             
	if m.group(2)=="amp" : #sugkrisi toy group(2) 
		return '&'
	if m.group(2)=="gt" :
		return '>'
	if m.group(2)=="lt" :
		return '<'
	if m.group(2)=="nbsp" :
		return ' '

rexp = re.compile(r'(<title>)(.+?)</title>',re.DOTALL) #prwto zhtoumeno eksagwgh titlou 
rexp1 = re.compile(r'<!--(.+?)-->',re.DOTALL)  #apalifh twn sxoliwn
rexp2 = re.compile(r'(<script(.+?)</script>)|(<style(.+?)</style>)',re.DOTALL) #apalifh srcipt kai style
rexp3 = re.compile(r'(<a)(.+?)/a>',re.DOTALL) # ebresh <a> kai </a> 
rexp4 = re.compile(r'href="(.[^"]+?)(">)([^<].+?)(<)',re.DOTALL) # href
rexp5 = re.compile(r'<(.+?)>',re.DOTALL) #evresh olwn twn tags
rexp6 = re.compile(r'(&)(.+?);',re.DOTALL) #evresh twn eisodwn poy ksekinan me & kai teleiwnoun se ;
rexp7 = re.compile(r'\s+') #evresh kenwn kai newlines
with open('testpage.txt','r') as fp: #anagnwsh testpage.html
	text = fp.read()
	f = open("output.txt","w+") #anoigma neou arxeiou gia write
	for m in rexp.finditer(text): #xrhsh finditer
		print(m.group(2),file=f) #ektipwsh periexomenou titlou
	newtext = rexp1.sub('',text) # me thn rexp1 antikathistoume ta sxolia me keno
	newtext1 = rexp2.sub('',newtext) #apalifh twn oswn tha brei h rexp2 dld script kai style
	for m2 in rexp3.finditer(newtext1): #gia kathe <a> </a>
		for m3 in rexp4.finditer(m2.group(2)): #briskw to href pou perilambanetai sto <a> </a>
			print(m3.group(1),m3.group(3), file=f) #ektypwnw (sto arxeio output.txt) me thn xrhsh twn groups to link kai titlo
	#se kapoia idiothta href to link htan to javascript:void(0) kai sthn thesh tou titlou perieixe &lt gia paradeigma, to krathsa ws link k titlo 
	newtext2 = rexp5.sub('',newtext1) # antikatastash oswn briskei h rexp5 me keno(apalifh twn sxoliwn)
	newtext3 = rexp6.sub(repl,newtext2) #allagh twn oswn briskei h rexp6 (&amp;, &gt;..)me bash thn sunartish repl(nomizw omws oti exoun hdh afairethei dioti briskontousan se tags kai oxi sto keimeno pou exei meinei ws edw) 	
	newtext4 = rexp7.sub(' ',newtext3) #apalifh twn kenwn kai new lines me mono ena keno
	print(newtext4, file=f) #ektypwsh sto arxeio 

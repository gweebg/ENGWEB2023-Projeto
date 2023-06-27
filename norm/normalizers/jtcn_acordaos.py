from utils import readInputData,normDesc,writeOutputData,emptyValue,handleProcesso,recorrido,legislação,areaTematica,jurisprudências,referencias,tribunalRecorrido
import re
data=readInputData("/jtcn_acordaos.py")
maxReadFile=1E9



def apendice(item,k):
    if k not in [ "Processo","Secção","Data do Acordão","Tribunal","Relator","Descritores","Sumário","Recorrente","Votação","Meio Processual","Parecer Ministério Publico","url","tribunal","Texto Integral","Decisão","Critério"]:
        if k in item["Processo"] or ("Texto Integral" in item.keys() and k in item["Texto Integral"]):
            if 'Apêndice' not in item.keys():
                item['Apêndice']=""
            item['Apêndice']+= f"{k} : {item[k]}\n"
            del item[k]
            
def handleTextoIntegral(item,k):
    if k=="Decisão Texto Integral":
        item["Texto Integral"]=item[k]
        del item[k] 
                

for item in data:
    for key in list(item.keys()):
        emptyValue(item,key)
    for key in list(item.keys()):
        recorrido(item,key)
        handleTextoIntegral(item,key)
        referencias(item,key)
        legislação(item,key)
        tribunalRecorrido(item,key)
        
    for key in list(item.keys()):
        apendice(item,key)

        
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]
    normDesc(item)

    
    
writeOutputData("/jtcn_acordaos.py",data)
        

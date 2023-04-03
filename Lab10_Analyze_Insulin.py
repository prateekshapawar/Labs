i="ORIGIN"\
        "1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed"\
       "61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"\
"//"\
#malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn
i=i.replace("ORIGIN","")
i=i.replace(" ","")
i=i.replace("1","")
i=i.replace("6","")
i=i.replace("1","")
i=i.replace("/","")
i=i.replace("/","")

print("Full range of insulin:",i)
print("No. of characters in insulin:",len(i))

lsinsulin=i[0:24]
print("A] lsinsulin range is:",lsinsulin)
print("No. of characters in lsinsulin:",len(lsinsulin))

binsulin=i[24:54]
print("B] binsulin range is:",binsulin)
print("No. of characters in binsulin:",len(binsulin))

cinsulin=i[54:89]
print("C] binsulin range is:",cinsulin)
print("No. of characters in insulin:",len(cinsulin))

ainsulin=i[89:110]
print("D] ainsulin range is:",ainsulin)
print("No. of characters in ainsulin:",len(ainsulin))
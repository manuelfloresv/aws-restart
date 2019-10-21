import xml.etree.ElementTree as ETree

outfile="INSD.json"

infile=open("INSD.xml", "a")
with open(outfile, "a") as f:
    seqinfilecount = 0
    context = ETree.iterparse(infile, events=("start", "end"))
    for event, elem in context:
        if event == "end" and elem.tag == "INSDSeq":
            ETObj = elem
            if ETree.iselement(ETObj):
                try:
                    insertdict = selectid(ETObj)
                except:
                    raise ValueError("no seq-id")
                insertdict["divid"] = divid
                remainingdict = presqlprocessing(insertdict)
                if ifnotset:
                    print(ifnotset)
            seqinfilecount += 1
            print(seqinfilecount)
            elem.clear()
print("{} errors ({}%) in inserting from file {} ({}) seqs analyzed".format(dividfileerrorcounter, 100 * (float( dividfileerrorcounter) / float(seqinfilecount)),\
  countfiles, seqinfilecount))  
seqcount = seqcount + seqinfilecount  
connect.close()              
print("{} seqs analyzed in 1 file".format(len(insertdict)))

seq_a = "HSVNLLEDSHNGKLCRLKGIAPLQLGNCSIAGWILGNPECESLFSKESWSYFAETPNSENGTCYPGYFADYEELREQLSSVSSFERFEIFPKESSWPNHTVTKGVTASCSHNGKSSFYRNLLWLTEKNGLYPNLSKSYVNNKEKEVLVLWGVHHPSNIGDQRAIYHT"
seq_b = "HSVNLLEDSHNGKLCLLKGIAPLQLGNCSVAGWILGNPECELLISKESWSYIVETPNPENGTCYPGYFADYEELREQLSSVSSFERFEIFPKGSSWPNHTVT_GVSASCSHNGKSSFYRNLLWLTGKNGLYPNLSMSYVNNKEKEVLVLWGVHHPPNIGDQRALYHT"    
len_a = len(seq_a)    
len_b = len(seq_b)    
print("Length of Sequence A: " + str(len_a))    
print()    
print("Length of Sequence B: " + str(len_b))
print()

def sequence_compare(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  mismatches.append('|')
              else:
                  mismatches.append(' ')
        print (seq_a)
        print ("".join(mismatches))
        print (seq_b)

def sequence_compare_index(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  mismatches.append(str(pos))
              else:
                  mismatches.append(' ')
        print (seq_a)
        print ("".join(mismatches))
        print (seq_b)

def sequence_compare_index2(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  mismatches.append(str(pos))

        print ("\n".join(mismatches))


sequence_compare(seq_a,seq_b) # Print the sequence and changes with |
print("\n\n")
sequence_compare_index(seq_a,seq_b) # # Print the sequence and changes with index
print("\n\n")
sequence_compare_index2(seq_a,seq_b) # Print the index only





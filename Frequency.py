ency = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

englishFreq = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']

ency2 = ency.replace(" ", "")
freq = {}
  
for i in ency2:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sorted_freq = sorted(freq.items(), key = lambda kv: kv[1],reverse=True)

sorted_freq = dict(sorted_freq)
print("This is how many times the characters are frequent in this passage:\n", sorted_freq)

#englishFreq = {'a' :0.0817,'b' : 0.0150,'c': 0.0278,'d': 0.0425,'e':0.1270,'f':0.0223,'g':0.0202,'h':0.0609,'i':0.0697,'j':0.0015,'k':0.0077,'l':0.0403,'m':0.0241,'n':0.0675,'o':0.0751,'p':0.0193,'q':0.0010,'r':0.059,'s':0.063,'t':0.0906,'u':0.0276,'v':0.0098,'w':0.0236,'x':0.0015,'y':0.0197,'z':0.0007}
#sorted_eng = sorted(englishFreq.items(), key = lambda kv: kv[1],reverse=True)
print("\n\nThis is the the frequency in the English alphabet(Going from highest to lowest): \n", englishFreq)
final_dict = dict(zip(list(sorted_freq.keys()), englishFreq))
print("\n\n This is the matching of characters from the text given and english letters:\n", final_dict)

solution = ""
for char in ency:
    if char == ' ':
        solution += ' '
    else:
        solution += final_dict[char]
print("\n\nThis is the final result:\n",solution)



from django.shortcuts import render
from django.utils import timezone
from .models import *
from .forms import *
from .forms import SystemForm
from django.http import *
from django.shortcuts import render_to_response
import re
from django.http import HttpResponse
import json


# Create your views here.
def main_page(request):
    return render(request, 'cryptapp/main_page.html', {})

def system_feature(request):
    return render(request, 'cryptapp/system_feature.html', {})

def about_us(request):
    return render(request, 'cryptapp/about_us.html', {})



def issues(request):
    return render(request, 'cryptapp/issues.html', {})

def data(fl_name):
    w=fl_name.objects.all().values_list('word', flat=True)
    lst=[]
    for word in w:
        lst.append(str(word))
    return lst

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            fb = form.save(commit = False)
            fb.published_date = timezone.now()
            fb.save()
            return HttpResponseRedirect('/thanks/') 
    else:
        form = ContactForm()
    return render(request, 'cryptapp/contact.html', {'form':form})

def thanks(request):
	return render(request, 'cryptapp/thanks.html', {})

def feedback(request):
    if request.method == 'POST':
        form = FbackForm(data=request.POST)
        if form.is_valid():
            fb = form.save(commit = False)
            fb.published_date = timezone.now()
            fb.save()
            return HttpResponseRedirect('/thanks/') 
    else:
        form = FbackForm()
    return render(request, 'cryptapp/feedback.html', {'form': form})


def system(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SystemForm(data=request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            fb = form.save(commit = False)
            fb.save()
            cd = form.cleaned_data
            #vcipher=valid_cipher(cd.get('cipher'))
            return render_to_response('cryptapp/system.html',{'form':form})
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SystemForm()

    return render(request, 'cryptapp/system.html', {'form': form})

#to check whether cipher is valid or not
# def valid_cipher(c):
#     res=""
#     match = re.match(r'^[A-Za-z ]*$', c)
#     if not match:
#         res="Invalid CipherText"
#     else:
#         res="Valid CipherText"
#     return res
def spell_check(word):
    #checks the spelling of the word and returns true if the spelling is correct
    global tw,trw,fw
    if ((len(word) == 2)):
        #if two-letter word
        if word in tw:
            return True
    if ((len(word) == 3)):
        #if three-letter word
        if word in trw:
            return True
    if ((len(word) == 4)):
        #if four-letter word
        if word in fw:
            return True
    if ((len(word) > 4) ):
        return True
    return False

def replacefunc(word,file_word):
    #replaces the word passed with a word from file
        global sent,assumption
        for w,c in zip(word,file_word):
            if w.islower():
                if c not in assumption.values():
                    sent = sent.replace(w, c)
                    assumption[w]=c
                    

def one_letter():
    global sent,assumption,one_w,ow,cnt1
    
    for i in range(0,len(one_w)):
            sent = sent.replace(one_w[i], ow[i])
            cnt1=1
            assumption[one_w[i]]=ow[i]

def find_key(value):
    global assumption
    for k,v in assumption.items():
        if v== value:
            return k

def revert_trans():
    global sent,a_sent,assumption
    k=[] 
    v=[]

    sent = a_sent
    for w in sent:
        if w.isupper():
            k.append((find_key(w)))
            v.append(w)
    
    assumption.clear()
    for i in range(len(k)):
        assumption[k[i]]=v[i]
    #assumption = a_assump
    

def trans_status():
    global sent
    for w in sent.split():
        if len(w) >1:
            
            if not spell_check(w):
                revert_trans()
                return False
    return True            


def pattern(word,fil,cnt):
        #word: word from sentence containing a capital letter
        #fil: corresponding file(e.g 4_word file for 4-letter word)
        #cnt: counter that mentions position in the file
        #pattern function replaces the words from list with suitable word from file according to conditions if a pattern is matched
        global b_done,sent,assumption,cnt1,cnt2,cnt3,cnt4,cnti4,cnti3,cntn3,cntn4,s2cnt,e2cnt,nfw,ntrw,itrw,ifw,efw,etrw,etw,sfw,strw,stw
        pat=""
        c=0
        n=cnt
        wd=word
        i=0
        mtch = []
        j=[]
        #check if a letter occurs more than once in the word(for e.g in THAT, T occurs twice)
        for w in word:
                wc = 0
                if w.islower():
                    wc = word.count(w)
                    
                    if wc>1:
                        
                        j.append((word.index(w)))   #append both the index of occurrence
                        fil = mtch          #replace the file with another list
        
        #append all the words from file in which a letter occur more than once
        if fil == mtch:
            for wrd in fil:
                if wrd[j[0]] == wrd[j[1]]:
                    fil.append(wrd)
            
        #replace all the small letters in the word with "." for pattern matching
        for w in word:
                wc = 0
                if w.islower():
                    word=word.replace(w,'.')                   
                
        #match the word with every word from file and replace with the first pattern match found. 
        for ch in fil:
            n+=1    
            if re.match(word,ch):
                pat= ch
                replacefunc(wd,pat)
                c=1     #implies pattern is found  
                break
            cnt+=1
        
        #if no pattern is matched call backtrack
        if (n == len(fil)):
            if not c:
                return sent
                #backtrack(wd)
                
        if sent.isupper():
            main()

def pat_rep(lst,prfil,cnt):
    #lst:list of specific words(i.e 2-letter, 3-letter etc) in the sentence containing cipher letters.
    #fil:text file of containing 2-letter,3-letter etc plain-letter words corresponding to list.
    #cnt:counter to mention the position in the file
    #pat_rep function replaces the words from list with suitable word from file according to condition.
    global b_done,sent,assumption,cnt1,cnt2,cnt3,cnt4,cnti4,cnti3,cntn3,cntn4,s2cnt,e2cnt,nfw,ntrw,itrw,ifw,efw,etrw,etw,sfw,strw,stw
    lfil=prfil
    lcnt=cnt
    j=0
    
    for word in lst:
        ind=lst.index(word)
        lst_len=len(lst[0])
        lst=[]
        
        for strng in sent.split():
            if len(strng)==lst_len :
                lst.append(strng)
        word=lst[ind]
        prfil = lfil
        i = lst.index(word)     #index of word in list
        cnt_cap=0               #counter for capital letter in a word
        for t in word:
            #if a letter in word of list is already in assumption replace the cipher-letter with 
            #corresponding plainletter entry in assumption
            if t in assumption:     
                word=word.replace(t,assumption[t])
                t=t.replace(t,assumption[t])
            #if a letter in word is capital increase counter
            if t.isupper():
                cnt_cap+=1
                
       
        
        j = (sent.split()).index(word)      #index of word in original sentence which is modified
        

        if len(word)==2:
            if j==0:
                prfil = stw
                cnt=s2cnt
            elif j==len(sent.split())-1:
                prfil = etw
                cnt=e2cnt
            # else:
            #     fil = lfil
            #     cnt=lcnt
            #     print lfil

        if len(word) == 3 and prfil!=ntrw and prfil!=pfw:
            
            #if a 3-letter word is in starting/ending position then replace the file with another file containing 
            #all possible 3-letter words which can come at starting or ending
            if j==0:
                prfil = strw
                cnt=s3cnt
            elif j==len(sent.split())-1:
                prfil = etrw
                cnt=e3cnt
            # else:
            #     fil = lfil
            #     cnt=lcnt
        if len(word) == 4 and prfil!=nfw:
            #if a 4-letter word is in starting/ending position then replace the file with another file containing 
            #all possible 4-letter words which can come at starting or ending
            
            if j==0:
                prfil = sfw
                cnt=s4cnt
            elif j==len(sent.split())-1:
                prfil = efw
                cnt=e4cnt
            # else:
            #     fil = lfil
            #     cnt=lcnt
        lst[i] = word
        
        #if the word contains any capital letter then call pattern matching
        if cnt_cap>=1 and cnt_cap<len(word):
            
            pattern(word,prfil,cnt)
        #if the word does not contain any capital letter then replace the word with word in file 
        if cnt_cap==0:
            
            #start from the position of counter in the file
            while (cnt<len(prfil)):
                c=0
                #if the letter of word from file is already in assumption increase the counter to 
                #replace with the next word else replace with the same word
                for f in prfil[cnt]:
                    if f in assumption.values():
                        c=1
                if c>0:
                    cnt+=1
                if c==0:
                    replacefunc(word,prfil[cnt])
                    cnt+=1
                    break
        if len(word) == 2:
            cnt2 = cnt
        if len(word) == 3:
            cnt3 = cnt
        if len(word) == 4:
            cnt4 = cnt

def transposition():
    #checks if 
    global assumption,sent
    upper = []
    p = c =0
    for words in sent.split():
        for w in words:
            if w.isupper():
                key = find_key(w)
                
                p = ord(w.lower())
                c = ord(key)
                if p<c:
                    p=p+26

                upper.append(c-p)
                           
                
    upper = list(set(upper))
    
    if len(upper)==1:
        for words in sent.split():
            for w in words: 
                if w.islower():
                    pr = (ord(w) - upper[0])
                    if pr < 97:
                        pr = ord(w) + 26 - upper[0]
                    if pr > 122:
                        pr = ord(w) - 26 - upper[0]
                    pr = (chr(pr)).upper()
                    sent = sent.replace(w,pr)
                    assumption[w] = pr
                    #print assumption
                    #print sent
        #to check whether transposition is done or not
        return True
    return False

def main():
    global sent,trans_cnt,a_sent,main_cnt,one_w,two_w,three_w,four_w,gfour_w,pfour_w,cnt1,cnt2,cnt3,cnt4,cnti4,cnti3,cntn3,cntn4,s2cnt,e2cnt,nfw,ntrw,itrw,ifw,efw,etrw,etw,sfw,strw,stw
    t_d = 0
    t_nd=0
    main_cnt=main_cnt+1
    if main_cnt>1:
        one_w=[]
        two_w=[]
        three_w=[]
        gfour_w=[]
        four_w=[]
    final_cnt = 0

    for word in sent.split():
        if word.isupper() and spell_check(word)==True:
            final_cnt+=1
    if final_cnt != len(sent.split()):
        for word in words:
                if (len(word) == 1) :
                    if word.islower():
                        one_w.append(word)
        if one_w:
            one_letter()
            a_sent = sent #store sent before transposition
            
            if(trans_cnt<1):
                t1_done=transposition()
                trans_cnt+=1
                if t1_done:
                    status=trans_status()
                    if not status:
                        t_d=1
                    else:
                        return sent
                else:
                    t_d=1

        if (t_d==1 or len(one_w)==0 or trans_cnt>0) :
            

            # for finding pairs with I
            flag = 0
            s=sent.split()
            #for i in range(len(words)-1):
            if len(words[0])==1:
                if s[0]=='I':
                    
                    if (len(s[1])==2):
                        for w in s[1]:
                            if w in s[0]:
                                flag+=1
                        if flag==0:
                            replacefunc(s[1],'AM')
                    if (len(s[1])==3):
                        for w in s[1]:
                            if w in s[0]:
                                flag+=1
                        if flag==1:
                            if s[1].index(s[0])==1:
                                replacefunc(s[1],'DID')
                            else:
                                key=find_key('I')
                                sent=sent.replace('I',key)
                                del assumption[key]
                                replacefunc(key,'A')

                        if flag==0:
                            replacefunc(s[1],itrw[cnti3])
                    if (len(s[1])==4):
                        for w in s[1]:
                            if w in s[0]:
                                flag+=1
                        if flag==1:
                            if s[1].index(s[0])==1:
                                if s[1][-1]==s[1][-2]: 
                                    replacefunc(s[1],'WILL')
                                else:
                                   replacefunc(s[1],'LIKE') 
                            else:
                                key=find_key('I')
                                sent=sent.replace('I',key)
                                del assumption[key]
                                replacefunc(key,'A')

                        if flag==0:
                            replacefunc(s[1],ifw[cnti4])

            # for words having two letters
            for word in sent.split():
                   if (len(word) == 2) :
                        if not word.isupper():
                            two_w.append(word)
                            
                   
            if two_w:
                pat_rep(two_w,tw,cnt2) 
                a_sent = sent 
                if not one_w and trans_cnt<1:
                    t_done=transposition()
                    trans_cnt+=1
                    if t_done:
                        status=trans_status()
                        if not status:
                            t_d=1
                        else:
                            return sent
                    else:
                        t_d=1
                
            
            #checking A-noun pair
            s1 = sent.split()
            nf=nt=[]
            for i in range(len(s1)-1):
                if len(s1[i])==1:
                    if s1[i]=='A':
                        
                        if len(s1[i+1])==3:
                            nt.append(s1[i+1])
                            pat_rep(nt,ntrw,cntn3)
                        if len(s1[i+1])==4:
                            nf.append(s1[i+1])
                            pat_rep(nf,nfw,cntn4)
            return sent
            if (t_d==1 or trans_cnt>0 ) :                
                # for words having three letters
                for word in sent.split():
                    if ((len(word) == 3) and (word not in three_w)):
                        if not word.isupper():
                            three_w.append(word)
                if three_w:
                    pat_rep(three_w,trw,cnt3)
                    
            #     # for words havin double letter
            #     # for word in sent.split():
            #     #     if (len(word) > 2):
            #     #         double_letter(word)

            #     # for words having four letters
            #     for word in sent.split():
            #         if ((len(word) == 4) and (word not in four_w) ):
            #             if not word.isupper():
            #                 four_w.append(word)
            #     if four_w:
            #         pat_rep(four_w,fw,cnt4)

            #     for word in sent.split():
            #         if ((len(word) > 4) and (word not in gfour_w) ):
            #             if not word.isupper():
            #                 gfour_w.append(word)
            #     if gfour_w:
            #         for i in range(len(gfour_w)):
            #             for j in range(0,2):
            #                 if gfour_w[i][j].islower():
            #                     if i==1:
            #                         if gfour_w[i][j+1].islower():
            #                             pfour_w.append(gfour_w[i][:3])
            #                         else:
            #                             pfour_w.append(gfour_w[i][:2])
            #                     break
            #             if pfour_w:
            #                 pat_rep(pfour_w,pfw,cntp)


                    
    else:
    #     grammar_test.main(sent)
        return sent

def getresult(request,cipher):
    global sent,trans_cnt,a_sent,main_cnt,one_w,two_w,three_w,four_w,gfour_w,pfour_w,words,assumption,ow,tw,trw,fw,cnt1,cnt2,cnt3,cnt4,cnti4,cnti3,cntn3,cntn4,s2cnt,e2cnt,nfw,ntrw,itrw,ifw,efw,etrw,etw,sfw,strw,stw
    sent = cipher
    match = re.match(r'^[A-Za-z ]*$', sent)
    # err="Invalid ciphertext"
    if not match:
        return HttpResponse(json.dumps("Invalid CipherText"))
        #result(err)
        #mainloop()

    else:
        trans_cnt=0
        sent = sent.lower()
        words = sent.split()
        main_cnt=0
        b_done=0
        cnt1=cnt2=cnt3=cnt4=cnti3=cnti4=cntn3=cntn4=s2cnt=e2cnt= 0
        s3cnt=e3cnt=s4cnt=e4cnt=cntp=cnts=0
        assumption = {}
        assertion = {}
        one_w = []
        a_sent = sent
        two_w = []
        three_w = []
        four_w = []
        gfour_w=[]
        pfour_w=[]
        double_w = []

        ow = data(single_word)
        tw = data(double_word)
        trw = data(three_word)
        fw = data(four_word)
        nfw = data(four_letter_noun)
        ntrw = data(three_letter_noun)
        itrw = data(I_3word)
        ifw = data(I_4word)
        efw = data(e_4word)
        etrw = data(e_3word)
        etw = data(e_2word)
        sfw = data(st_4word)
        strw = data(st_3word)
        stw = data(st_2word)


        final_result  = main()
        
        return HttpResponse(json.dumps(final_result))

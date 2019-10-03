#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('--shady underground club simulation 1.0--')
a=int(input('age:'))
if a >= 18 and a<65:
    d=input('clothes color:')
    if d == 'black':
        d1=1
        m=input('how much money u have:')
        m_int= int(m)
        if m_int < 25:
            print('not enough mate')
            print('--end of simulation')
        else:
            print('go in')
            input()
            print('--end of simulation--')
    else:
        print('you dont really fit here...')
        m=input('...how much money you have:')
        m_int=int(m)
        if m_int >= 50:
            dr=input('got drugs with u (y/n):')
            if dr=='y':
                print('gimmie some')
                aaa=input('y/n:')
                if aaa=='y':
                    print('come on get in')
                    t=input('')
                    if t == 'thanks':
                        print('youre welcome')
                        print('--end of simulation--')
                    else:
                        print('go the fuck away disrespectful muthafaka')
                        print('-end of simulation-')
                else:
                    print('you cant enter then, greedy boy')
                    print('--end of simulation--')
            else:
                print('go get some and try again...')
                print('--end of simulation--')
        else:
            print('not enough mate...')
            br=input('ok i really have:')
            brint=int(br)
            if brint>=100:
                print('ok asshole get in')
                print('--end of simulation--')
            else:
                print('not even close, go home or ill kick you')
                print('--end of simulation')
elif a>65:
    print('you think u funny grampa? get the fuck away')
    print('--end of simulation')
else:
    print('too young, go home dude')
    print('--end of simulation')
           


# In[ ]:





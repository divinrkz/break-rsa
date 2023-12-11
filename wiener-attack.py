from fractions import Fraction
import math


def continued_fraction(e, N):
    cfs = []
    r = Fraction(e, N)
    while N:
        i = math.floor(r)
        cfs.append(i)
        f = r - i
        if f == 0:
            break
        else: 
            r = Fraction(1, f)
    return cfs

def convergents_of_cf(cfs):
    h, k = 1, 0
    h_prev, k_prev = 0, 1
    for q in cfs:
        h, h_prev = q*h + h_prev, h
        k, k_prev = q*k + k_prev, k
        yield h, k

def wiener_attack(e, N):
    for k, d in convergents_of_cf(continued_fraction(e, N)):
        if k == 0:
            continue
        potential_phi = (e*d - 1) // k
        p,q = solve(1, (-1 * (N - potential_phi + 1)), N)
        if p*q == N:
             return p,q   


def solve(a, b, c):
    from decimal import Decimal, getcontext
    getcontext().prec = 1000
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    return (int((-b + (b**2 - 4*a*c).sqrt())/(2*a)), int((-b - (b**2 - 4*a*c).sqrt())/(2*a)))

# N = 90581
# e = 17993

# N = 8812043537783992834592375402234870396641825341735701299647176256406599732968051770896882160923003833607299964801885015125425072360113606481397109880575698038805771666789634268060640489589352918776370339512697574115046707945166768935552152018424854018421507242016690189690266914976937170694781207628295144600321937961426645440171812433532486834824184790042133755824432752358221659006307494585013997639562241058478170234884138716515700636502484016416273137975716040363780457577708511916105622536896977870481033894682349535070299894064419115975355100527113719155875811681020802476667931645594671094318025099949648383347
# e = 3228301342303266421169117315760265758438425860657333023075829597552395212017796436911884275287966390407617802938724178366942194466205728470372043216608939456839954804786845175572213108129436795860389845100258566530684300969970499328655564039032662829299392356057113051321831341669257402651049244123195487871856258909824305976896584963016002994071619237976649996978528290124785498221252353608474821043968908499822252891280270405656437751865360460356950820053427716165084853009640829990558003626707620986873873743136655180285723789801432322989392606784278059858329547458885482252281296914966739731284337574001556313361

N = 13275993855447827057905575316152928933803559713561038486953556955295528774181862206805700546600906242564213981921365567995067466223388392052345549916385464010898896186245856602835178578423440480066592376460007112733599649807691968226433519496264529549808697687991163817510668677624950462967083150968059963277221081933239285021940877379067473095833217383645672515635215388294566119680851302961902254719359648080957083556347400462816497046344173078168361688270854607093902592058539570737961357033856659209349287236681426501482268591633258592399958227708167643570575052735251331518114924442746592771217694695504776276961
e = 686945467898625994329567239853219367023319662974164265414848213376155919639065255850427710622133826887012997577205546189566842185614676300310551686510418475520097270226500394372126574437409734435424145135351350185787850014506314815332805839568818571969476062251364009529744489560312798302342868820698396019545480910977382059035476856234130583710844660675709637272256599063035035258056132429807747785354614488875836317279566987664938388955897915721718845675625619089171343696325164644080703161269182642531060514790579887141870151118520705807547129934812039734842603015299505413097056641604844102873006636917657600017

p,q = wiener_attack(e, N)
print(f"p: {p}\nq: {q}")
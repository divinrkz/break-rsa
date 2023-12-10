# Break RSA.

## 1. Small $e$ Decryption.
I claim that just doing `pow(c, 1/e)` in python, which returns *eth* root of *C* successfully decrypts the encrypted message.
#### <ins>Proof</ins>
Let $C$ be the encrypted message, $M$ be the original message, $e$ be public key for encryption, and $N = pq$, where $p, q$ are large primes. Note that, we denote the private key pair as $(d, N)$. By the basic principle of RSA, the encryption of the message $M$ is given by $C \equiv M^e$ mod $N$ and the decryption of text $C$ is given by $C^{d}\equiv (M^{e})^{d}\equiv M^{ed}\equiv M$ mod $N$.
Since $e$ is small, $m^e$ < $N$, and it follows that $C = M^e$ *mod* $N = M^e$. So, $M = C^{\frac{1}{e}} = \sqrt[e]{C}$. <br> Therefore, my claim holds.

## 2. Wiener's Attack
Given an RSA key $(𝑁, 𝑒, 𝑑, 𝑝, 𝑞)$ with $𝑞 < 𝑝 < 2𝑞$ and $𝑑 < \frac{𝑁^\frac{1}{4}}{3}$ then an attacker can efficiently recover the entire private key: $(𝑑, 𝑝, 𝑞).$ 
## <ins>Proof</ins>

Note that by definition of RSA $ed \equiv $ $_{\phi(N)} 1$, so there exists a $k \in \mathbb{Z}$ such that $ed - k\phi(N) = 1$, by diving all the terms by $d\phi(N)$, it follows that, $\frac{e}{\phi(N)} - \frac{k}{d} = \frac{1}{d\phi(N)}$

By Legendre's Theorem, 
if $\lvert a - \frac{b}{c}\rvert < \frac{1}{2c^2}$ and $gcd(b,c)=1$ then $\frac{b}{c}$ appears as some convergent of a continued fraction of $a$ *(Read about [Continued Fractions](https://en.wikipedia.org/wiki/Continued_fraction)).* 

I claim that $a = \frac{e}{\phi(N)}$ with $\frac{b}{c} = \frac{k}{d}$ satisfies preconditions of Legendre's theorem that is $gcd(k,d)=1$ and $\lvert \frac{e}{\phi(N)} - \frac{k}{d}\rvert = \frac{1}{d\phi(N)} < \frac{2}{dN} < \frac{1}{2d^2}$.

<ins>Proof</ins>
<!-- 
Let $C = M^e$ *mod* $N$, where $C$ is the encrypted message, M is the original message, $N = pq$, and $e$ is public key for encryption.
Note that, we denote the private key pair as $(d, N)$. The encryption of the message $M$ is given by $C \equiv M^e$ mod $N$ and the decryption of  text $C$ is given by $C^{d}\equiv (M^{e})^{d}\equiv M^{ed}\equiv M$ mod $N$. <br>

Let $N = pq$ be an RSA-modulus, where $p$ and $q$ are primes of equal bit-size. <br>
Let $e$ be the public exponent and $d$ be the secret exponent satisfying
$ed = 1$ *mod* $\phi(N)$, where $\phi(N) = (p-1)(q-1)$ is the Euler's phi function. <br>
Note that we denote by $Z^*_{\phi(N)}$
the multiplicative group of invertible integers modulo $\phi(N)$. An RSA public key
is a tuple $(N, e)$ ∈ $Z * Z^*_{\phi(N)}$
$\phi(N)$.

Since $ed = 1$ *mod* $\phi(N)$, there exists a $k$ such that $ed - k\phi(N) = 1$. Therefore, by diving all terms by $d\phi(N)$, it follows that, $|\frac{e}{\phi(N)} - \frac{k}{d} = \frac{1}{d\phi(N)}|$.

Let G =  --> 

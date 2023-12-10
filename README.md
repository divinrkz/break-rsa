# Break RSA.

## 1. Small $e$ Decryption.
I claim that just doing `pow(c, 1/e)` in python, which returns *eth* root of *C* successfully decrypts the encrypted message.
### <ins>Proof</ins>
Let $C$ be the encrypted message, $M$ be the original message, $e$ be public key for encryption, and $N = pq$, where $p, q$ are large primes. Note that, we denote the private key pair as $(d, N)$. By the basic principle of RSA, the encryption of the message $M$ is given by $C \equiv M^e$ mod $N$ and the decryption of text $C$ is given by $C^{d}\equiv (M^{e})^{d}\equiv M^{ed}\equiv M$ mod $N$.
Since $e$ is small, $m^e$ < $N$, and it follows that $C = M^e$ *mod* $N = M^e$. So, $M = C^{\frac{1}{e}} = \sqrt[e]{C}$. <br> Therefore, my claim holds.

## 2. Wiener's Attack
Given an RSA key $(𝑁, 𝑒, 𝑑, 𝑝, 𝑞)$ with $𝑞 < 𝑝 < 2𝑞$ and $𝑑 < \frac{𝑁^\frac{1}{4}}{3}$ then an attacker can efficiently recover the entire private key: $(𝑑, 𝑝, 𝑞).$ 
### <ins>Proof</ins>

Note that by definition of RSA $ed \equiv $ $_{\phi(N)} 1$, so there exists a $k \in \mathbb{Z}$ such that $ed - k\phi(N) = 1$, by diving all the terms by $d\phi(N)$, it follows that, $\frac{e}{\phi(N)} - \frac{k}{d} = \frac{1}{d\phi(N)}$

By Legendre's Theorem, 
if $\lvert a - \frac{b}{c}\rvert < \frac{1}{2c^2}$ and $gcd(b,c)=1$ then $\frac{b}{c}$ appears as some convergent of a continued fraction of $a$ *(Read about [Continued Fractions](https://en.wikipedia.org/wiki/Continued_fraction)).* 


I claim that $a = \frac{e}{\phi(N)}$ with $\frac{b}{c} = \frac{k}{d}$ satisfies preconditions of Legendre's theorem that is $gcd(k,d)=1$ and $\lvert \frac{e}{\phi(N)} - \frac{k}{d}\rvert = \frac{1}{d\phi(N)} < \frac{2}{dN} < \frac{1}{2d^2}$.

<ins>Proof</ins><br>
Assume that $p$ and $q$ are large, precisely $p, q \geq 11$.<br>
Note that, $gcd(k,d) | k,  \iff \exists (a \in \mathbb{Z})$ where $a(\gcd(k, d)) = k$, and, $\gcd(k,d) | d,  \iff \exists (b \in \mathbb{Z})$ where  $b(\gcd(k, d)) = d.$
<br> By definition of RSA, $ed - k\phi(N) = 1$ ,it follows that, 
$\begin{equation}
    \begin{split}
        e(b(gcd(k, d))) - a(gcd(k, d))\phi(N) &= 1 \quad \quad\\
        gcd(k, d)(eb - a\phi(N)) &= 1 \quad \quad 
    \end{split}
\end{equation}$
By definition of divides, $x | y \iff \exists(k \in \mathbb{Z}) 
, y = kx$, where $y = 1, x = \gcd(k,d),  k = (eb-a\phi(N))$[because we know that $e,b,a,\phi(N)$ are integers, so the expression will also give an integer result]. Since $gcd(k,d)|1$, $\gcd(k,d)=1$. <br> Therefore, our claim holds.

Note that, $\lvert\frac{e}{\phi(N)} - \frac{k}{d}\rvert =  \lvert\frac{ed - k\phi(N)}{d\phi(N)}\rvert$. <br> Since we know that $ed - k\phi(N) = 1$, we have $ \lvert\frac{ed - k\phi(N)}{d\phi(N)}\rvert = \frac{1}{d\phi(N)}$. 
<br> 

Since, we assumed that $q>11$,
$
\begin{equation}
    \begin{split}
        3q^2 - 6q + 2 &> 0  \\
        4q^2 - q^2 - 6q + 2 &> 0 \\
        2(2q)q-6q + 2 &> q^2 \quad\quad \\
        2(2q)q - 2(3q)+2 > 2pq - 2(p+q) + 2 > pq &> q^2 \quad\quad \\
        2(p-1)(q-1) &> pq \quad\quad\\
        2\phi(N) &> N \quad\quad \\
        \phi(N) & > \frac{N}{2}\quad\quad \\
        \frac{1}{\phi(N)} &< \frac{2}{N}\quad\quad \\
         \frac{1}{d\phi(N)} &< \frac{2}{dN} 
    \end{split}
\end{equation}
$
Note that, $d < \frac{N^{\frac{1}{4}}}{3} = 3d < N^{\frac{1}{4}} = (3d)^4 < N $, which is: $ \frac{1}{(3d)^4} > \frac{1}{N}$ \\
So, $\frac{2}{dN} = \frac{2}{d}\frac{1}{N} < \frac{2}{d}\frac{1}{81d^4} = \frac{2}{81d^5} < \frac{1}{2d^2}$. 

Therefore, I've shown that $\left\lvert\frac{e}{\phi(N)} - \frac{k}{d}\right\lvert = \frac{1}{d\phi(N)} < \frac{2}{dN} < \frac{1}{2d^2}$ 

<br>
<br>

Note that by defintion of $\phi(N) = (p-1)(q-1)$, $N=pq$. 
So, $|pq - (p-1)(q-1)| = |pq-(pq-p-q-1)| = |p+q-1|$. By assumption, $p,q  \geq 11$, so $|p+q-1| > 0$ and so, we can write $p+q-1$. We also know that $p < 2q$. So $p+q-1 < 2q+q-1 = 3q-1 < 3q = 3\sqrt{q^2} < 3\sqrt{pq} = 3\sqrt{N}$.<br>
Therefore, $\left\lvert N − \phi(N)\right\rvert < 3\sqrt{N}$

<br>

Note that,
$
\begin{equation}
 \begin{split}
    \left\lvert\frac{e}{N} - \frac{k}{d}\right\lvert &= \left\lvert\frac{ed - kN}{Nd} \right\lvert\\
    &= \left\lvert\frac{ed-k\phi(N) - kN + k\phi(N)}{Nd}\right\lvert \\
    &= \left\lvert\frac{1-k(N-\phi(N))}{Nd}\right\lvert  \\
    &< \frac{-k(N-\phi(N))}{Nd} \\
       &< \left\lvert k \frac{3\sqrt{N}}{Nd}\right\lvert 
       = \left\lvert\frac{3k\sqrt{N}}{\sqrt{N}\sqrt{N}d}\right\lvert  
       < \frac{3k}{d\sqrt{N}}
     \end{split}
\end{equation}
$
<br>

From $ed - k\phi(N)=1, k\phi(N) = ed - 1 < ed$ which is $k\phi(N) < ed$. Since, $e < \phi(N)$, so $k\phi(N) < ed < \phi(N)d$ then we have $k\phi(N) < \phi(N)d = k < d$.<br>
Therefore, $k < d$


Since I've shown that $k < d$, and $d < \frac{N^{\frac{1}{4}}}{3}$ , we have $|\frac{e}{N} - \frac{k}{d}| < \frac{1}{d}N^{\frac{1}{4}}$ \\
Since $d < \frac{N^{\frac{1}{4}}}{3}, 3d < N^\frac{1}{4}, 2d < 3d < N^\frac{1}{4}$, thus we have $2d < N^\frac{1}{4}$ then, $\frac{1}{2d} > \frac{1}{N\frac{1}{4}}$. <br>From this we can conclude that $|\frac{e}{N} - \frac{k}{d}| < \frac{3k}{d\sqrt{N}} < \frac{1}{d^2d} = \frac{1}{2d^2}$ \\
Therefore we are done.
\end{part}
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

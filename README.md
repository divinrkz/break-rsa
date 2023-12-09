#
Proof of the programs.

### Small $e$ Decryption.
I claim that just doing `pow(c, 1/e)` in python, which returns *eth* root of *C* successfully decrypts the encrypted message.
#### Proof
Let $C$ be the encrypted message, $M$ be the original message, $e$ be public key for encryption, and $N = pq$, where $p, q$ are large primes. <br>
Note that, we denote the private key pair as $(d, N)$. By the basic principle of RSA, the encryption of the message $M$ is given by $C \equiv M^e$ mod $N$ and the decryption of  text $C$ is given by $C^{d}\equiv (M^{e})^{d}\equiv M^{ed}\equiv M$ mod $N$. <br>
Since $e$ is small, $m^e$ < $N$, and it follows that $C = M^e$ *mod* $N = M^e$. So, $M = C^{\frac{1}{e}} = \sqrt[e]{C}$. <br> So my claim holds.

<!-- 
### Proof
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

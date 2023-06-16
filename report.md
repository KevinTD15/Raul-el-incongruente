# Diseño y Análisis de Algoritmos
## Kevin Talavera Díaz - C411
## Sergio Pérez Pantoja - C411

<br>

## Raul el incongruente.

<br>

Raul últimamente quiere impresionar a su novia Daniela, para esto va usar sus habilidades matemáticas, ya que Daniela tiene varias amigos en la facultad y puede apreciar las peripecias de Raul. Raul le pedirá a cada uno de los n amigos matemáticos de Daniela que le diga 2 numeros $a_i$, $b_i$, el segundo mayor o igual que el primero.

Ahora Raul va a efectuar su acto de alta pericia Matemática sin la ayuda siquiera de calculadora, Raul dirá un número entero x, tal que para todos los pares dichos por los amigos de Daniela, x no será congruente $a_i$ módulo $b_i$.

<br>

## Nociones de congruencia:

<br>

### Teorema de congruencia lineal:

<br>

Si a y b dos números enteros cualesquiera y n es un número entero positivo, entonces la congruencia: 

$ax \equiv b (mod \text{ } n)$

tiene una solución para x si y solo si b es divisible por el máximo común divisor de a y n (denotado mediante $mcd(a,n)$). Cuando éste es el caso, y $x_0$ es una solución de la ecuación, entonces el conjunto de todas las soluciones está dado por:

$$ x_0 + k \frac {n}{d} | k \in Z$$

En particular, existirán exactamente $d = mcd(a,n)$ soluciones en el conjunto de residuos $0, 1, 2, .., n-1$

<br>

### Sistema de congruencias lineales:

<br>

Sean $m1$ y $m2$ dos naturales primos entre sí. Si cada una de las congruencias lineales:

$a_1x \equiv b_1$ ($mod$ $m_1$)

$a_2x \equiv b_2$ ($mod$ $m_2$)

Tiene solución, entonces existe solución común a ambas congruencias en  $Z$. Si, además, $mcd (a1,m1) = 1$ y $mcd (a2, m2) = 1$, dicha solución es única

<br>

### Teorema chino del resto:

<br>

Supongamos que $n_1, n_2, .., n_k$ son enteros positivos coprimos dos a dos. Entonces, para enteros dados $a_1, a_2, .., a_k$, existe un entero $x$ que resuelve el sistema de congruencias simultáneas

$x \equiv a_1$ ($mod$ $n_1$)

$x \equiv a_2$ ($mod$ $n_2$)

$...$

$x \equiv a_k$ ($mod$ $n_k$)

Más aún, todas las soluciones x de este sistema son congruentes módulo el producto $N$ $= n_1 * n_2 * n_3$.

De manera más general, las congruencias simultáneas pueden ser resueltas si los $n_i$'s son coprimos a pares. Una solución $x$ existe si y solo si:

$a_i \equiv a_j$ ($mod$ $mcd(n_i, n_j)$) $\forall i, j$.

Todas las soluciones $x$ son entonces congruentes módulo el $mcm(n_i)$ $\forall i$

<br>

## Ejemplo de solución:

<br>

...

<br>

## Complejidad:

<br>

Este es un problema que pertenece al conjunto conocido como **NP-Completos**.

<br>

### Demostración:

<br>

Para demostrar que este problema es **NP-Completo** es necesario demostrar que es **NP** y **NP-Duro**.

<br>

### NP:

<br>

Esta parte de la demostración es relativamente sencilla ya que basta con demostrar que la verificación de cualquier candidato a solución puede ser resuelta en tiempo polinomial, lo cual es verdad debido a que: Sea $x$ el valor candidato a solución, se desea verificar si $x$ es incongruente con todas las ecuaciones de congruencia del sistema. Esto se realiza sustituyendo en cada una de las ecuaciones el valor de $x$ y verificando si existe solución para ese valor. Por lo que queda demostrado que el problema es **NP**.

<br>

### NP-Duro:

<br>

En esta parte de la demostración se tratará de reducir el bien conocido problema **NP** **3-SAT**.

... Explicacion de 3SAT...

La reducción consiste en asignarle a cada variable de la fórmula lógica un numero primo que la represente, por tanto el primer paso es elegir $p_1, p_2, .., p_n$ donde $p$ es un número primo (para poder aplicar el teorema chino del resto visto anteriormente) y $n$ es el número de variables.

De esta forma cada cláusula del problema **3-SAT** es codificada como un sistema de congruencias de la forma:

- Sea $V$ el conjunto de variables de la fórmula lógica:

$\forall v \in V \text{ } \exists {\text{ } a \equiv b \text{ } (mod \text{ } p)}$ donde $b \in {1, 0}$ en dependencia si la variable aparece negada o no respectivamente y $p$ es el número primo asociado a $v$.

Luego, por cada cláusula, se agrupan las ecuaciones de congruencia que se correspondan con sus respectivas variables. Por ejemplo:

- Sea $x \lor \lnot y \lor z$ la i-ésima cláusula de la fórmula y $p_1, p_2, p_3$ sus primos asociados respectivamente:

Se obtienen las siguientes ecuaciones:

$a_i \equiv 0$ ($mod$ $p_1$)

$a_i \equiv 1$ ($mod$ $p_2$)

$a_i \equiv 0$ ($mod$ $p_3$)

Al resolver el sistema de congruencias usando el teorema chino del resto se obtendrá el conjunto de valores de $a$ tales que $a$ sea congruente con los sistemas de congruencias lineales correspondientes a cada cláusula.

*Hasta este momento todo lo explicado han sido transformaciones necesarias para poder reducir una entrada de **3-SAT** a nuestro problema, las cuales son todas polinomiales.*

Por último se crea una ecuación de congruencia con cada uno de los resultados de la siguiente forma:

$x \not \equiv a_1$ ($mod$ $p_1 * p_2 * p_3$)

$x \not \equiv a_2$ ($mod$ $p_1 * p_2 * p_3$)

$...$

$x \not \equiv a_n$ ($mod$ $p_1 * p_2 * p_3$)

Este sistema coincide con nuestro problema inicial de incongruencias simultáneas, luego, si se logra encontrar un valor de $x$ tal que $x$ sea incongruente a todos en el sistema, la fórmula lógica de es satisfacible, en caso contrario, no lo es, debido a esto la transformación de la salida de nuestro problema a la salida de **3-SAT** es también polinomial, por lo que queda demostrado que nuestro problema es tan o más difícil que **3-SAT** por lo que nuestro problema es **NP-Duro**.

Como ya se demostró que este problema es **NP** y **NP-Duro**, queda demostrado que el problema de Incongruencias simultáneas es **NP-Completo**.



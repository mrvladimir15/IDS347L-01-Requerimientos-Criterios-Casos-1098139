# Preguntas

**1. ¿Qué es un Coding Dojo?**
> En esencia, es una reunión de un grupo de programadores con el propósito de completar un reto de programación. Este encuentro persigue la diversión de los miembros, a la vez que el aumento de prácticas de programación; como resultado, guía a los programadores a mejorar sus habilidades.

**2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia.**
> * **Requerimientos**. Son propiedades del software que deben ser exhibidas con el propósito de resolver un problema del mundo real. En palabras llanas, es lo que el cliente o usuario necesitan que haga el software, a fin de resolver una necesidad. Por ejemplo, para una aplicación de caja: *la caja debe aceptar la entrada y salida de efectivo*.
> * **Criterios de aceptación**. Se trata de enunciados que indican características con las cuales debe cumplir el software construido para avalar que sus requerimientos son cumplidos satisfactoriamente.  Por ejemplo, para una aplicación de caja: *el estado de pago de una factura debe ser 'pendiente' hasta que el cliente realice el desembolso por el monto total de dicha factura*.
> * **Casos**. Son ejemplos de escenarios por los cuales atravesará el software para validar un criterio de aceptación. Para una aplicación de caja: *El cliente suministra un monto insuficiente para saldar una factura*.

**3. Dé dos ejemplos de requerimientos no-funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.).**
> * **Requerimiento de portabilidad**. La aplicación debe ser ejecutable en el sistema operativo Windows 10 Home.
> * **Requerimiento de eficiencia**. La aplicación debe cargar la información de un cliente en un tiempo inferior a 7 segundos.

**4. ¿Qué es TDD?**
> Es la sigla para *Test Driven Development*; es un marco de desarrollo que implica diseñar, crear y ejecutar los casos de prueba para una aplicación **previo** a la codificación ideada inicialmente. Si dichos casos de prueba fallan, entonces se codifica una posible nueva solución, con el objetivo de que esta supere el caso de prueba. Este acercamiento persigue crear un código más limpio y libre de bugs.

**5. ¿Qué son pruebas unitarias automatizadas?**
> Son pequeñas pruebas automatizadas realizadas por un software para este propósito, las cuales implican evaluar componentes pequeños y/o puntuales de una aplicación. Son utilizadas para probar el nivel del código e intentar localizar errores en sus funciones, métodos y rutinas.

**6. ¿Cuál fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?**
> El primer framework de pruebas unitarias es JUnit, creado para Java en 1997.

**7. Describa los componentes de la arquitectura xUnit.**
> * **Ejecutor de pruebas/Test runner**. Es un programa ejecutable que corre las pruebas implementadas utilizando un framework de xUnit y reportando los resultados de dichas pruebas.
> * **Casos de prueba/Test case**. Es la clase más esencial de la arquitectura xUnit; todsa las pruebas unitarias son heredadas a partir de esta.
> * **Banco de pruebas/Test fixtures**. Es la serie de precondiciones o estados que necesita ejecutar una prueba. El desarrollador debería configurar un buen estado conocido previo a las pruebas, y, regresar al estado original tras las pruebas.
> * **Paquete de pruebas/Test suites**. Es un conjunto de pruebas que comparten el mismo banco de pruebas, en consecuencia, el orden de estas pruebas no debería importar.
> * **Ejecución de la prueba/Test execution**. Es la ejecución de una prueba unitaria, que contiene dos métodos utilizados para inicializar y limpiar los bancos de pruebas tras las pruebas: setup() y teardown().
> * **Formateador de resultados de pruebas/Test result formatter**. El ejecutor de la prueba produce resultados en uno o más formatos. Regularmente, existe un formateador de resultados, cuyo propósito es producir una salida en el formato XML.

**8. Indique al menos tres desventajas de las pruebas unitarias automatizadas.**
> * Son mucho más costosas que las pruebas manuales.
> * Se torna agobiante decidir quién automatizará y quién formalizará las pruebas.
> * Está limitado a algunas organizaciones, pues, muchas prefieren prescindir de la automatización de pruebas.
> * Las pruebas automatizadas requieren personas con habilidades y formación para llevarlas a cabo.
> * Las pruebas automatizadas solo eliminan la labor "mecánica" de ejecutar el proceso de pruebas, pero, la creación de casos de pruebas aún requiere de profesionales en pruebas.

**9. Indique al menos tres ventajas de las pruebas unitarias automatizadas.**
> * **Costo más bajo**. A pesar de que implican un costo inicial superior, la automatización de pruebas unitarias permite ahorrar costos de mantenimiento frente a las pruebas manuales.
> * **Seguridad de la información**. En ocassiones, cuando el proyecto no es automatizado, los encargados de pruebas pueden no dedicar todo el tiempo que requiere el proceso de pruebas, provocando que código defectuoso pase a producción. Las pruebas automatizadas brindan un sistema más denso de seguridad a través de controles continuos para este propósito, superando el potencial inconveniente mencionado previamente con relación a las pruebas manuales.
> * **Retroalimentación más rápida**. Dada su mayor eficiencia y rapidez, estas pruebas ofrecen resultados más rápidos a los interesados del proyecto, como clientes, usuarios y equipo de desarrollo. Por tanto, los errores pueden ser localizados y corregidos con mayor rapidez.
> * **Mayor motivación del equipo**. A razón de su eficiencia, el equipo de desarrollo tiene una respuesta más rápida, evitando que sus miembros se desmotiven y sientan insatisfacción, ambas sensaciones generadas a razón de la espera tardía de una retroalimentación.
> * **Aserción/assertion**. Es una función macro que verifica el comportamiento o estado de la unidad que está bajo prueba. Por lo general, las aserciones expresan la condición lógica que es verdadera para los resultados esperados en un sistema bajo prueba ejecutado correctamente.

# Referencias bibliográficas
* Briceño, G. (2020, 30 marzo). Pruebas Automatizadas: tipos y conceptos erróneos. Club de Tecnología. https://www.clubdetecnologia.net/blog/2020/pruebas-automatizadas-tipos-y-conceptos-erroneos/
* Colaboradores de Wikipedia. (2022, marzo 7). JUnit. Wikipedia. https://en.wikipedia.org/wiki/JUnit
* Colaboradores de Wikipedia. (2022, mayo 13). XUnit. Wikipedia. https://en.wikipedia.org/wiki/XUnit
* GeeksforGeeks. (2020, 2 marzo). Advantages and Disadvantages of Automated Testing. https://www.geeksforgeeks.org/advantages-and-disadvantages-of-automated-testing/
* Hamilton, T. (2022, 30 abril). What is Test Driven Development (TDD)? Tutorial with Example. Guru99. https://www.guru99.com/test-driven-development.html
* Ramos, L. (2020, 27 enero). Los beneficios de las pruebas automatizadas. Auditeste. https://auditeste.com.br/es/beneficios-testes-automatizados/
* Solano, L. (2012, 10 septiembre). What is Coding Dojo. Lorenzo Solano Martinez. https://lorenzosolano.com/what-is-coding-dojo/  
* Solano, L. (2017, 18 junio). Requirements, Acceptance Criteria, and Scenarios. Lorenzo Solano Martinez. https://lorenzosolano.com/requirements-acceptance-criteria-and/
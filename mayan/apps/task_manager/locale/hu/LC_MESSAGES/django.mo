��    "      ,  /   <      �  	   �               "  2   1  �   d     �  �   �     �     �     �     �     �     �  ]   �  S   [     �  
   �     �     �     �  
   �     �       
   $  r   /  j   �  �        �  
   �     �     �     �  j  �     e
     r
     �
     �
  S   �
  �     L  �  �             #  
   0     ;     R  9   X  t   �  c        k  
   p  !   {  &   �  
   �     �     �  %   �       �   $  t   �  �        �               )     D                           "                                !                                                                                            	   
    Arguments Background task workers Celery Default queue? Default: "AMQPLAIN". Set custom amqp login method. Default: "Disabled". Toggles SSL usage on broker connection and SSL settings. The valid values for this option vary by transport. Default: "amqp://". Default broker URL. This must be a URL in the form of: transport://userid:password@hostname:port/virtual_host Only the scheme part (transport://) is required, the rest is optional, and defaults to the specific transports default values. Default: No result backend enabled by default. The backend used to store task results (tombstones). Refer to http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend Dotted path Host Is transient? Keyword arguments Label Low latency, long lived tasks Maximum amount of resident memory a worker can execute before it's replaced by a new process. Maximum number of tasks a worker can execute before it's replaced by a new process. Name Nice level Queue: %s, not found Queues for worker: %s Schedule Start time Task manager Task types for queue: %s Test queue The nice value determines the priority of the process. A higher value lowers the priority. The default value is 0. The number of worker processes/threads to launch. Defaults to the number of CPUs available on the machine. Transient queues are not persistent. Tasks in a transient queue are lost if the broker is restarted. Transient queues use less resources and managed non critical tasks. Type View tasks Worker list Worker process ID Worker: %s, not found Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-07-11 12:52+0000
Last-Translator: Csaba Tarjányi, 2024
Language-Team: Hungarian (https://app.transifex.com/rosarior/teams/13584/hu/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: hu
Plural-Forms: nplurals=2; plural=(n != 1);
 Argumentumok Háttérfeladat worker-ek Celery Alapértelmezett várólista? Alapértelmezett\: "AMQPLAIN". Egyéni amqp bejelentkezési módszer beállítása. Alapértelmezett: "Letiltva". Az SSL-használat bekapcsolása a brókerkapcsolat és az SSL-beállítások esetén. Ennek az opciónak az érvényes értékei szállításonként változnak. Alapértelmezett: "amqp://". Alapértelmezett bróker URL. Ennek az URL-nek a következő formájúnak kell lennie: transport://userid:password@hostname:port/virtual_host Csak a séma része (transport://) kötelező, a többi rész opcionális, és alapértelmezésként az adott szállítás alapértelmezett értékeit veszi fel. Alapértelmezett: Alapértelmezés szerint nincs engedélyezve az eredményháttér. A feladatok eredményeinek (tombstones) tárolására használt backend. Lásd: http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend. Pontozott elérési út Kiszolgáló Átmeneti? Kulcsszó paraméterek Cimke Alacsony késleltetésű, hosszú élettartamú feladatok A rezidens memória maximális mennyisége, amelyet egy worker végrehajthat, mielőtt egy új processz váltja fel. Egy worker által végrehajtható feladatok maximális száma, mielőtt új folyamatra cserélnék. Név Nice szint Várólista: %s , nem található Várólisták a workerek számára: %s Ütemezés Kezdési idő Feladatkezelő Feladattípusok a várólistához: %s Teszt várólista A nice érték határozza meg a folyamat prioritását. A magasabb érték csökkenti a prioritást. Az alapértelmezett érték 0. Az indítandó munkafolyamatok/szálak száma. Alapértelmezés szerint a gépen rendelkezésre álló CPU-k száma. Az átmeneti várólisták nem tartósak. Az átmeneti várólistában lévő feladatok elvesznek, ha a bróker újraindul. A tranziens várólisták kevesebb erőforrást használnak, és nem kritikus feladatokat kezelnek. Típus Feladatok megtekintése Worker lista Worker folyamatazonosító Worker: %s , nem található 
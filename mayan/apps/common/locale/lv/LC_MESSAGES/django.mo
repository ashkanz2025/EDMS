��    �      $  �   ,      �
      �
        (   #  )   L  )   v      �  B  �      s      �  :   �  +  �  �        �  
   �     �     �       )        5     M     a  ,   h  	   �     �  -   �     �     �                 #   "  	   F     P  	   ^     h     m     u    v  �   y  2  �  u  2  ^   �  8     �   @  C     �   \  2  !  �   T"  �  I#  �   �$  b   �%  �  �%     �'     �(     �(     �(     �(     �(     �(  (   �(     )     ")  F   +)  N   r)     �)     �)     �)     �)     *     
*     *  Q   *     j*  1   p*     �*     �*     �*     �*     �*     �*  �   �*  &   u+  	   �+  ,   �+     �+  ^   �+     F,     b,     g,  %   n,  =   �,     �,     �,  
   �,  H   �,     F-  	   M-  �   W-  �   .  	   �.     �.     �.     �.     �.     �.     /     /  d   /  b   z/  �   �/    �0  O   �1  3   42  0   h2  I   �2  M   �2     13     :3  3   @3    t3  ;   �4     �4     �4     �4     �4  x  5  w   �6  �  �6      �8      �8  ,   �8  +   �8  0   9  #   M9  9  q9  4  �:  e  �;  }  F=  O   �@  "  A  �   7C     $D     (D  	   0D  	   :D     DD  =   TD     �D     �D  	   �D  -   �D     �D  *   E  +   .E     ZE     bE     uE     �E     �E  <   �E     �E     �E     �E     F     F  (  F  
  AG  �   LH  M  �H  �  BJ  j   �K  F   ML  �   �L  M   �M  �   �M  �  �N  �   zR  �  iS  �   U  m   �U  �  ]V  <  X  '   AY     iY     �Y     �Y     �Y     �Y  J   �Y      Z     6Z  W   DZ  `   �Z     �Z     [     7[     R[     [[     b[     h[  S   x[     �[  6   �[     
\     \     \     !\     8\  !   A\  �   c\  -   �\     !]  4   .]     c]  m   �]  %   �]     ^     #^  /   +^  M   [^     �^     �^     �^  J   �^  
   &_     1_  �   =_  �   !`  	   a     a     a  &   )a  $   Pa     ua     ~a     �a  r   �a  p   b  �   tb  $  mc  Q   �d  /   �d  4   e  C   Ie  h   �e  
   �e     f  ,   f  O  4f  A   �g  
   �g  !   �g  !   �g     h  �  /h  �   �i     e          ^       4       n   "       2      j   \   {       �   9   s       S       R   q                 U   u   X   7   r          o   c       '   	          d          ,   B           H       _   .                  =   
           l       b      %                 +   |   &   1   ;      -       $   Q   h       I   8   0   C   )   L       �       3   y          g   x   G   *   #   V   :   }           k   [   E   6       ?                      /       F   A   i             O   ]   M   `   m      Z   @      D   !   f   t      ~   W   z           v   Y   <   N      w              p   a           >   5         T   J   (      P   K                       %(object)s created successfully. %(object)s deleted successfully. %(object)s not created, error: %(error)s %(object)s not deleted, error: %(error)s. %(object)s not updated, error: %(error)s. %(object)s updated successfully. A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database. The DATABASES setting must configure a default database; any number of additional databases may also be specified. A list of IP addresses, as strings, that: Allow the debug() context processor to add some variables to the template context. Can use the admindocs bookmarklets even if not logged in as a staff user. Are marked as "internal" (as opposed to "EXTERNAL") in AdminEmailHandler emails. A list of all available languages. The list is a list of two-tuples in the format (language code, language name) for example, ('ja', 'Japanese'). This specifies which languages are available for language selection. Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages.  A list of strings representing the host/domain names that this site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. Values in this list can be fully qualified names (e.g. 'www.example.com'), in which case they will be matched against the request's Host header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: '.example.com' will match example.com, www.example.com, and any other subdomain of example.com. A value of '*' will match anything; in this case you are responsible to provide your own validation of the Host header (perhaps in a middleware; if so this middleware must be listed first in MIDDLEWARE). A storage backend that all workers can use to share files. A string representing the language code for this installation. This should be in standard language ID format. For example, U.S. English is "en-us". It serves two purposes: If the locale middleware isn't in use, it decides which translation is served to all users. If the locale middleware is active, it provides a fallback language in case the user's preferred language can't be determined or is not supported by the website. It also provides the fallback translation when a translation for a given literal doesn't exist for the user's preferred language. A string representing the time zone for this installation. Note that this isn't necessarily the time zone of the server. For example, one server may serve multiple Django-powered sites, each with a separate time zone setting. About About this Actions Add Add all Automatically enable logging to all apps. Available attributes: 
 Available fields: 
 Celery Checks proper formatting of the README file. Clear all Clear error log entries for: %s Command line environment with autocompletion. Common Common periodic Confirm Confirm delete Create Current user locale profile details Dashboard Date and time Date time Days Default Default: "amqp://". Default broker URL. This must be a URL in the form of: transport://userid:password@hostname:port/virtual_host Only the scheme part (transport://) is required, the rest is optional, and defaults to the specific transports default values. Default: '' (Empty string). Password to use for the SMTP server defined in EMAIL_HOST. This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server. If either of these settings is empty, Django won't attempt authentication. Default: '' (Empty string). Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won't attempt authentication. Default: '/accounts/login/' The URL where requests are redirected for login, especially when using the login_required() decorator. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: '/accounts/profile/' The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter. This is used by the login_required() decorator, for example. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: 'django.core.mail.backends.smtp.EmailBackend'. The backend to use for sending emails. Default: 'localhost'. The host to use for sending email. Default: 'webmaster@localhost' Default email address to use for various automated correspondence from the site manager(s). This doesn't include error messages sent to ADMINS and MANAGERS; for that, see SERVER_EMAIL. Default: 25. Port to use for the SMTP server defined in EMAIL_HOST. Default: 2621440 (i.e. 2.5 MB). The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See Managing files for details. See also DATA_UPLOAD_MAX_MEMORY_SIZE. Default: 2621440 (i.e. 2.5 MB). The maximum size in bytes that a request body may be before a SuspiciousOperation (RequestDataTooBig) is raised. The check is done when accessing request.body or request.POST and is calculated against the total request size excluding any file upload data. You can set this to None to disable the check. Applications that are expected to receive unusually large form posts should tune this setting. The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don't typically perform deep request inspection, it's not possible to perform a similar check at that level. See also FILE_UPLOAD_MAX_MEMORY_SIZE. Default: False. Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging connections, see the implicit TLS setting EMAIL_USE_SSL. Default: False. Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465. If you are experiencing problems, see the explicit TLS setting EMAIL_USE_TLS. Note that EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only set one of those settings to True. Default: No result backend enabled by default. The backend used to store task results (tombstones). Refer to http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend Default: None. Specifies a timeout in seconds for blocking operations like the connection attempt. Default: None. The URL where requests are redirected after a user logs out using LogoutView (if the view doesn't get a next_page argument). If None, no redirect will be performed and the logout view will be rendered. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: [] (Empty list). List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bad robots/crawlers. This is only used if CommonMiddleware is installed (see Middleware). Delete stale uploads Details for: %s Django Documentation Duplicate data error: %(error)s Edit %s Edit current user locale profile details Edit locale profile Edit: %s Enable error logging outside of the system error logging capabilities. Enter a valid 'internal name' consisting of letters, numbers, and underscores. Error log entries Error log entries for: %s Error log entry Errors Facet File Filename Force the conversion of the database even if the receiving database is not empty. Forum Here you can configure all aspects of the system. Hours Language License Locale profile Minutes Must select at least one item. Name of the view attached to the brand anchor in the main menu. This is also the view to which users will be redirected after log in. Name to be displayed in the main menu. Namespace No %(verbose_name)s found matching the query No action selected. No results here means that don't have the required permissions to perform administrative task. No setup options available. None Object Object error log cleared successfully Path to the logfile that will track errors during production. Provides style checking. Remove Remove all Restricts dumped data to the specified app_label or app_label.ModelName. Result Secondary Select entries to be added. Hold Control to select multiple entries. Once the selection is complete, click the button below or double click the list to activate the action. Select entries to be removed. Hold Control to select multiple entries. Once the selection is complete, click the button below or double click the list to activate the action. Selection Setup Setup items Shared uploaded file Shared uploaded files Source code Support System The database from which data will be exported. If omitted the database named "default" will be used. The database to which data will be imported. If omitted the database named "default" will be used. The file storage engine to use when collecting static files with the collectstatic management command. A ready-to-use instance of the storage backend defined in this setting can be found at django.contrib.staticfiles.storage.staticfiles_storage. The full Python path of the WSGI application object that Django's built-in servers (e.g. runserver) will use. The django-admin startproject management command will create a simple wsgi.py file with an application callable in it, and point this setting to that application. The list of validators that are used to check the strength of user's passwords. The number objects that will be displayed per page. These modules are used to do system maintenance. This feature has been deprecated and will be removed in a future version. Time to delay background tasks that depend on a database commit to propagate. Timezone Tools URL of the installation or homepage of the project. URL to use when referring to static files located in STATIC_ROOT. Example: "/static/" or "http://static.example.com/" If not None, this will be used as the base path for asset definitions (the Media class) and the staticfiles app. It must end in a slash if set to a non-empty value. Used to allow offline translation of the code text strings. User User locale profile User locale profiles View error log When set to True, if the request URL does not match any of the patterns in the URLconf and it doesn't end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost. The APPEND_SLASH setting is only used if CommonMiddleware is installed (see Middleware). See also PREPEND_WWW. Your database backend is set to use SQLite. SQLite should only be used for development and testing, not for production. Project-Id-Version: Mayan EDMS
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2019-06-29 06:21+0000
Last-Translator: Roberto Rosario
Language-Team: Latvian (http://www.transifex.com/rosarior/mayan-edms/language/lv/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: lv
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2);
 %(object)s izveidots veiksmīgi. %(object)s veiksmīgi izdzēsts. %(object)s nav izveidots, kļūda: %(error)s %(object)s nav dzēsts, kļūda: %(error)s. %(object)s nav atjaunināts, kļūda: %(error)s. %(object)s veiksmīgi atjaunināts. Vārdnīca ar visu Django lietojamo datu bāzu iestatījumiem. Tā ir ligzdota vārdnīca, kuras saturs iezīmē datubāzes aizstājvārdu vārdnīcā, kurā ir atsevišķas datu bāzes iespējas. DATABASES iestatījumam jākonfigurē noklusējuma datu bāze; var norādīt arī jebkuru papildu datu bāzu skaitu. IP adrešu saraksts kā virknes, kas: Ļauj atkļūdošanas () konteksta procesoram pievienot dažus mainīgos veidnes kontekstam. Var izmantot admindocs grāmatzīmes, pat ja nav pieteicies kā personāla lietotājs. Tiek atzīmēti kā "iekšējie" (atšķirībā no "EXTERNAL") AdminEmailHandler e-pastos. Visu pieejamo valodu saraksts. Sarakstā ir iekļauts divu ierakstu saraksts (valodas kods, valodas nosaukums), piemēram, ('ja', 'japāņu'). Tas norāda, kuras valodas ir pieejamas valodas izvēlei. Parasti pietiek ar noklusējuma vērtību. Iestatiet šo iestatījumu tikai tad, ja vēlaties ierobežot valodu izvēli ar Django sniegto valodu apakškopu. Saraksts ar virknēm, kas pārstāv vietnes/domēna vārdus, kurus šī vietne var pasniegt. Šis ir drošības pasākums, lai novērstu HTTP uzņēmēja galvenes uzbrukumus, kas ir iespējami pat daudzās šķietami drošās tīmekļa servera konfigurācijās. Vērtības šajā sarakstā var būt pilnībā kvalificēti vārdi (piemēram, “www.example.com”), un tādā gadījumā tie tiks precīzi saskaņoti ar pieprasījuma Host galvenes virsrakstu (nejūtīga, neietverot portu). Vērtību, kas sākas ar punktu, var izmantot kā apakšdomēna aizstājējzīmi: '.example.com' atbilst example.com, www.example.com un jebkuram citam example.com apakšdomēnam. Vērtība '*' atbilst jebkuram; šajā gadījumā jūs esat atbildīgs par savas galvenes apstiprinājuma apstiprināšanu (varbūt starpprogrammatūrā; ja tā, tad starpprogrammatūra vispirms jānorāda iekš MIDDLEWARE). Uzglabāšanas backend, ko visi darbinieki var izmantot, lai koplietotu failus. Stringi, kas attēlo šīs instalācijas valodas kodu. Tam jābūt standarta valodas ID formātā. Piemēram, ASV angļu valoda ir "en-us". Tas kalpo diviem mērķiem: ja lokālā starpprogrammatūra netiek izmantota, tā nolemj, kurš tulkojums tiek nodrošināts visiem lietotājiem. Ja lokalizācijas starpprogrammatūra ir aktīva, tā nodrošina rezerves valodu, ja lietotāja vēlamo valodu nevar noteikt vai vietne to neatbalsta. Tā arī nodrošina rezerves tulkojumu, ja konkrētā literārā tulkojums nav lietotāja vēlamajai valodai. Virkne, kas attēlo šīs instalācijas laika joslu. Ņemiet vērā, ka tas ne vienmēr ir servera laika josla. Piemēram, viens serveris var kalpot vairākām Django darbinātām vietnēm, katra ar atsevišķu laika joslu iestatījumu. Par Par šo Darbības Pievienot Pievienot visus Automātiski iespējojiet pierakstīšanos visās lietotnēs. Pieejamie atribūti: 
 Pieejamie lauki: 
 Selerijas Pārbauda README faila pareizu formatēšanu. Iztīrīt visu Notīrīt kļūdas žurnāla ierakstus: %s Komandrindas vide ar automātisko aizpildi. Kopīgs Kopīgs periodiski Apstiprināt Apstipriniet dzēšanu Izveidot Pašreizējā lietotāja lokalizācijas profila informācija Panelis Datums un laiks Datums Laiks Dienas Noklusējums Noklusējums: "amqp://". Noklusējuma starpnieka URL. Tam ir jābūt URL šādā formā: transport://userid:password@hostname:port/virtual_host Nepieciešama tikai shēmas daļa (transport://), pārējais ir neobligāts, un pēc noklusējuma konkrētās transportēšanas noklusējuma vērtības. Noklusējums: '' (Tukša virkne). Parole, ko izmantot SMTP serverim, kas definēts vietnē EMAIL_HOST. Šis iestatījums tiek izmantots kopā ar EMAIL_HOST_USER autentificējot SMTP serveri. Ja kāds no šiem iestatījumiem ir tukšs, Django neveic autentifikāciju. Noklusējums: '' (Tukša virkne). Lietotājvārds, ko izmantot SMTP serverim, kas definēts pakalpojumā EMAIL_HOST. Ja tukšs, Django neizmēģinās autentifikāciju. Noklusējums: '/accounts/login/' URL, kurā pieprasījumi tiek novirzīti, lai pieteiktos, īpaši, ja izmantojat login_required () dekoratoru. Šis iestatījums arī pieņem nosauktos URL modeļus, kurus var izmantot, lai samazinātu konfigurācijas dublēšanos, jo jums nav jādefinē URL divās vietās (iestatījumi un URLconf). Noklusējums: '/accounts/profile/' URL, kurā pieprasījumi tiek novirzīti pēc pieteikšanās brīdī, kad skats par ieguldījumu.auth.login nesaņem nākamo parametru. To izmanto, piemēram, login_required () dekorētājs. Šis iestatījums arī pieņem nosauktos URL modeļus, kurus var izmantot, lai samazinātu konfigurācijas dublēšanos, jo jums nav jādefinē URL divās vietās (iestatījumi un URLconf). Noklusējums: “django.core.mail.backends.smtp.EmailBackend”. Backend, ko izmanto e-pasta sūtīšanai. Noklusējums: “localhost”. Hosts, ko izmanto e-pasta sūtīšanai. Noklusējums: “webmaster@localhost” Noklusējuma e-pasta adrese, ko izmanto dažādai automatizētai sarakstei no vietnes pārvaldnieka (-iem). Tas neietver kļūdas ziņojumus, kas nosūtīti ADMINS un MANAGERS; par to skatiet SERVER_EMAIL. Noklusējums: 25. Portu, ko izmantot SMTP serverim, kas definēts EMAIL_HOST. Noklusējums: 2621440 (ti, 2,5 MB). Maksimālais lielums (baitos), ko augšupielāde būs pirms straumēšanas datņu sistēmā. Papildinformāciju skatiet sadaļā Failu pārvaldīšana. Skatiet arī DATA_UPLOAD_MAX_MEMORY_SIZE. Noklusējums: 2621440 (ti, 2,5 MB). Maksimālais lielums baitos, ko pieprasīšanas struktūra var būt pirms aizdomīgas darbības (RequestDataTooBig) palielināšanas. Pārbaude tiek veikta, piekļūstot pieprasījumam.body vai request.POST, un tiek aprēķināta pēc kopējā pieprasījuma lieluma, izņemot visus failu augšupielādes datus. To var iestatīt uz Nav, lai izslēgtu pārbaudi. Lietojumprogrammām, kurām sagaidāms, ka tās saņems neparasti lielas veidlapas ziņas, ir jākontrolē šis iestatījums. Pieprasījuma datu apjoms ir saistīts ar atmiņas apjomu, kas nepieciešams, lai apstrādātu pieprasījumu un aizpildītu GET un POST vārdnīcas. Lielus pieprasījumus var izmantot kā pakalpojumu atteikšanas uzbrukuma vektoru, ja tas netiek pārbaudīts. Tā kā tīmekļa serveri parasti neveic dziļu pieprasījumu pārbaudi, nav iespējams veikt līdzīgu pārbaudi šajā līmenī. Skatiet arī FILE_UPLOAD_MAX_MEMORY_SIZE. Noklusējums: False. Vai lietojat TLS (drošu) savienojumu, runājot ar SMTP serveri. Tas tiek izmantots skaidriem TLS savienojumiem, parasti 587. portā. Ja rodas savienojumi ar kabeļiem, skatiet netiešo TLS iestatījumu EMAIL_USE_SSL. Noklusējums: False. Vai, runājot ar SMTP serveri, izmantojiet netiešu TLS (drošu) savienojumu. Vairumā e-pasta dokumentāciju šāda veida TLS savienojums tiek saukts par SSL. To parasti izmanto 465. portā. Ja rodas problēmas, skatiet skaidru TLS iestatījumu EMAIL_USE_TLS. Ņemiet vērā, ka EMAIL_USE_TLS/EMAIL_USE_SSL ir savstarpēji izslēdzoši, tāpēc tikai vienu no šiem iestatījumiem iestatiet uz True. Noklusējums: pēc noklusējuma nav iespējots rezultāts. Backend, ko izmanto uzdevumu rezultātu (kapu pieminekļu) glabāšanai. Skatiet http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend Noklusējums: nav. Norāda taimautu sekundēs, lai bloķētu darbības, piemēram, savienojuma mēģinājumu. Noklusējums: nav. URL, kurā pieprasījumi tiek novirzīti pēc tam, kad lietotājs ir pieteicies, izmantojot LogoutView (ja skats nesaņem nākamo lapu argumentu). Ja nav, netiks veikta novirzīšana un tiks atteikts logout skats. Šis iestatījums arī pieņem nosauktos URL modeļus, kurus var izmantot, lai samazinātu konfigurācijas dublēšanos, jo jums nav jādefinē URL divās vietās (iestatījumi un URLconf). Noklusējums: [] (Tukšs saraksts). Sastādīto regulāro izteiksmes objektu saraksts, kas pārstāv lietotāja-aģentu virknes, kurām nav atļauts apmeklēt jebkuru lapu. Izmantojiet to sliktiem robotiem/rāpuļprogrammām. Tas tiek izmantots tikai tad, ja ir instalēta CommonMiddleware (sk. Starpprogrammatūra). Dzēst nostāvējušās augšupielādes Sīkāka informācija par: %s Django Dokumentācija Datu kopijas kļūda: %(error)s Rediģēt %s Rediģējiet pašreizējās lietotāja lokalizācijas profila informāciju Rediģēt lokalizācijas profilu Rediģēt: %s Iespējot kļūdu reģistrēšanu ārpus sistēmas kļūdu reģistrēšanas iespējām. Ievadiet derīgu “iekšējo nosaukumu”, kas sastāv no burtiem, cipariem un pasvītrojumiem. Kļūdu žurnāla ieraksti Kļūdu žurnāla ieraksti: %s Kļūdu žurnāla ieraksts Kļūdas Fasets Fails Faila nosaukums Piespiest datu bāzes pārveidošanu pat tad, ja saņemošā datu bāze nav tukša. Forums Šeit jūs varat konfigurēt visus sistēmas aspektus. Stundas Valoda Licence Lokalizācijas profils Minūtes Jāizvēlas vismaz viens vienums. Zīmola enkuram pievienotā skata nosaukums galvenajā izvēlnē. Tas ir arī skats, uz kuru pēc pierakstīšanās lietotāji tiks novirzīti. Nosaukums, kas jārāda galvenajā izvēlnē. Vārda vieta %(verbose_name)s nav atrasts atbilstošs vaicājumam Nav atlasīta neviena darbība. Neviens no rezultātiem šeit nenozīmē, ka nav nepieciešamo atļauju administratīvā uzdevuma veikšanai. Nav pieejamas iestatīšanas opcijas. Nav neviens Objekts Objekta kļūdu žurnāls veiksmīgi notīrīts Ceļš uz žurnāla failu, kurā tiks novērotas kļūdas ražošanas laikā. Nodrošina stila pārbaudi. Noņemt Noņemt visus Ierobežo izgāztos datus uz norādīto app_label vai app_label.ModelName. Rezultāts Sekundārā Atlasiet pievienojamos ierakstus. Lai atlasītu vairākus ierakstus, turiet Control taustiņu. Kad atlase ir pabeigta, noklikšķiniet uz zemāk redzamās pogas vai veiciet dubultklikšķi uz saraksta, lai aktivizētu darbību. Atlasiet noņemamos ierakstus. Lai atlasītu vairākus ierakstus, turiet Control taustiņu. Kad atlase ir pabeigta, noklikšķiniet uz zemāk redzamās pogas vai veiciet dubultklikšķi uz saraksta, lai aktivizētu darbību. Selekcija Setup Iestatīšanas vienumi Koplietotais augšupielādētais fails Koplietotie augšupielādētie faili Pirmkods Atbalsts Sistēma Datu bāze, no kuras tiks eksportēti dati. Ja tas tiks izlaists, tiks izmantota datubāze ar nosaukumu "default". Datu bāze, uz kuru tiks importēti dati. Ja tas tiks izlaists, tiks izmantota datubāze ar nosaukumu "default". Failu glabāšanas dzinējs, ko izmanto, lai savāktu statiskos failus ar kolektīvās pārvaldības komandu. Šajā iestatījumā definētais glabāšanas backend piemērs ir pieejams vietnē django.contrib.staticfiles.storage.staticfiles_storage. Pilns Python ceļš WSGI lietojumprogrammas objektam, ko izmantos Django iebūvētie serveri (piemēram, palaišanas serveris). Django-admin startproject vadības komanda izveidos vienkāršu wsgi.py failu ar tajā pieprasāmo lietojumprogrammu un norādīs šo iestatījumu uz šo programmu. Validatoru saraksts, kurus izmanto, lai pārbaudītu lietotāja paroļu stiprumu. Objektu skaits, kas tiks rādīti vienā lapā. Šie moduļi tiek izmantoti sistēmas uzturēšanai. Šī funkcija ir novecojusi un tiks noņemta turpmākajā versijā. Laiks uz kādu aizkavēt fona uzdevumus, kas ir atkarīgs no datu bāzes apņemšanās uz izplatīšanu. Laika zona Rīki Projekta instalācijas vai mājas lapas URL. URL, kas jāizmanto, atsaucoties uz statiskiem failiem, kas atrodas STATIC_ROOT. Piemērs: "/static/" vai "http://static.example.com/". Ja šī vērtība nav tukša, tā tiks izmantota kā bāzes ceļš aktīvu definīcijām (multivides Media klase) un staticfiles lietotnei. Ja vērtība nav tukša, tai ir jābeidzas ar slīpsvītru. Izmantots, lai atļautu koda teksta virkņu bezsaistes tulkojumu. Lietotājs Lietotāja lokalizācijas profils Lietotāja lokalizācijas profili Skatīt kļūdu žurnālu Ja iestatījums ir True, un pieprasījuma URL neatbilst nevienam no URLconf modeļiem un tas nenotiek slīpsvītrā, HTTP novirzīšana tiek izdota tam pašam URL ar pievienoto slīpsvītru. Ņemiet vērā, ka novirzīšana var izraisīt jebkādu POST pieprasījumā iesniegto datu pazaudēšanu. Iestatījums APPEND_SLASH tiek izmantots tikai tad, ja ir instalēta CommonMiddleware (sk. Starpprogrammatūra). Skatiet arī PREPEND_WWW. Jūsu datubāzes backend ir iestatīts, lai izmantotu SQLite. SQLite jāizmanto tikai izstrādei un testēšanai, nevis ražošanai. 
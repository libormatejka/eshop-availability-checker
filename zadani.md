Potřebuji napsat colab google python script, který bude mít tyto požadavky:

- rozparsuje xml sitemapy
- v xml sitemapách zjistí, jestli se nachází konkrétní url, která bude obsahovat v <loc> substring

script bude mít config, ve které bude: 
- seznam url s xml, ve kterých <loc> hledat
- substring, který se bude hledat v <loc>
- script bude mít jednu buňku, kterou v colabu spustím
- hledaný substring bude pro všechny xml stejný.
- prohledávej pouze tyto xml, které budou v configu

Příklad:

<loc>https://www.xzone.cz/tomb-raider-legacy-of-atlantis-deluxe-edition-ps5</loc>

a hledaný substring bude tomb-raider-legacy-of-atlantis-deluxe-edition

v tom případě mi script najde a oznámí, že našel. Oznámení bude zatím jen výpisem, později uděláme e-mailovou notifikaci. Stačí mi nyní zakladní print do obrazovky.
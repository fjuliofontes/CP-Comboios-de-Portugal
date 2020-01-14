import sys, time

stations = {}
stationList = []

def initStations():
    stations["Abrantes".lower()] = "94-52001"
    stationList.append("Abrantes")

    stations["Ademia".lower()] = "94-36046";
    stationList.append("Ademia");

    stations["Afife".lower()] = "94-18119";
    stationList.append("Afife");

    stations["Agualva-Cacem".lower()] = "94-61002";
    stationList.append("Agualva-Cacem");

    stations["Aguas Santas - Palmilheira".lower()] = "94-3046";
    stationList.append("Aguas Santas - Palmilheira");

    stations["Aguda".lower()] = "94-39057";
    stationList.append("Aguda");

    stations["Agueda".lower()] = "94-42218";
    stationList.append("Agueda");

    stations["Aguieira".lower()] = "94-42267";
    stationList.append("Aguieira");

    stations["Aguim".lower()] = "94-37093";
    stationList.append("Aguim");

    stations["Albergaria dos Doze".lower()] = "94-34439";
    stationList.append("Albergaria dos Doze");

    stations["Albufeira - Ferreiras".lower()] = "94-78063";
    stationList.append("Albufeira - Ferreiras");

    stations["Alcacovas".lower()] = "94-74120";
    stationList.append("Alcacovas");

    stations["Alcaide".lower()] = "94-53504";
    stationList.append("Alcaide");

    stations["Alcains".lower()] = "94-53140";
    stationList.append("Alcains");

    stations["Alcantarilha".lower()] = "94-90092";
    stationList.append("Alcantarilha");

    stations["Alcaria".lower()] = "94-53629";
    stationList.append("Alcaria");

    stations["Aldeia".lower()] = "94-49411";
    stationList.append("Aldeia");

    stations["Alegria".lower()] = "94-11064";
    stationList.append("Alegria");

    stations["Alfarelos".lower()] = "94-35006";
    stationList.append("Alfarelos");

    stations["Alferrarede".lower()] = "94-52068";
    stationList.append("Alferrarede");

    stations["Algoz".lower()] = "94-90050";
    stationList.append("Algoz");

    stations["Alhandra".lower()] = "94-31237";
    stationList.append("Alhandra");

    stations["Almancil".lower()] = "94-78253";
    stationList.append("Almancil");

    stations["Almourol".lower()] = "94-51102";
    stationList.append("Almourol");

    stations["Alpedrinha".lower()] = "94-53355";
    stationList.append("Alpedrinha");

    stations["Alvaraes".lower()] = "94-6338";
    stationList.append("Alvaraes");

    stations["Alvega-Ortiga".lower()] = "94-52209";
    stationList.append("Alvega-Ortiga");

    stations["Alverca".lower()] = "94-31187";
    stationList.append("Alverca");

    stations["Alvito".lower()] = "94-74351";
    stationList.append("Alvito");

    stations["Ameal".lower()] = "94-35097";
    stationList.append("Ameal");

    stations["Amoreiras-Odemira".lower()] = "94-77099";
    stationList.append("Amoreiras-Odemira");

    stations["Ancora Praia".lower()] = "94-18150";
    stationList.append("Ancora Praia");

    stations["Aregos".lower()] = "94-9191";
    stationList.append("Aregos");

    stations["Areia-Darque".lower()] = "94-6395";
    stationList.append("Areia-Darque");

    stations["Arentim".lower()] = "94-29066";
    stationList.append("Arentim");

    stations["Areosa".lower()] = "94-18044";
    stationList.append("Areosa");

    stations["Arrifana".lower()] = "94-44248";
    stationList.append("Arrifana");

    stations["Arronches".lower()] = "94-57174";
    stationList.append("Arronches");

    stations["Assumar".lower()] = "94-57117";
    stationList.append("Assumar");

    stations["Avanca".lower()] = "94-38216";
    stationList.append("Avanca");

    stations["Aveiro".lower()] = "94-38000";
    stationList.append("Aveiro");

    stations["Aveleda".lower()] = "94-29108";
    stationList.append("Aveleda");

    stations["Azambuja".lower()] = "94-33001";
    stationList.append("Azambuja");

    stations["Azurva".lower()] = "94-42051";
    stationList.append("Azurva");

    stations["Badajoz".lower()] = "71-37606";
    stationList.append("Badajoz");

    stations["Baracal".lower()] = "94-48454";
    stationList.append("Baracal");

    stations["Barca da Amieira-Envendos".lower()] = "94-52415";
    stationList.append("Barca da Amieira-Envendos");

    stations["Barcelos".lower()] = "94-6122";
    stationList.append("Barcelos");

    stations["Barqueiros".lower()] = "94-9324";
    stationList.append("Barqueiros");

    stations["Barquinha".lower()] = "94-51045";
    stationList.append("Barquinha");

    stations["Barragem de Belver".lower()] = "94-52241";
    stationList.append("Barragem de Belver");

    stations["Barrimau".lower()] = "94-5058";
    stationList.append("Barrimau");

    stations["Barroselas".lower()] = "94-6304";
    stationList.append("Barroselas");

    stations["Beja".lower()] = "94-75002";
    stationList.append("Beja");

    stations["Belver".lower()] = "94-52282";
    stationList.append("Belver");

    stations["Bemposta".lower()] = "94-55129";
    stationList.append("Bemposta");

    stations["Bencanta".lower()] = "94-35170";
    stationList.append("Bencanta");

    stations["Benquerencas".lower()] = "94-52878";
    stationList.append("Benquerencas");

    stations["Bifurcacao de Lares".lower()] = "94-64022";
    stationList.append("Bifurcacao de Lares");

    stations["Bobadela".lower()] = "94-31070";
    stationList.append("Bobadela");

    stations["Boliqueime".lower()] = "94-78147";
    stationList.append("Boliqueime");

    stations["Bom Joao".lower()] = "94-73031";
    stationList.append("Bom Joao");

    stations["Bombarral".lower()] = "94-62703";
    stationList.append("Bombarral");

    stations["Braco de Prata".lower()] = "94-31005";
    stationList.append("Braco de Prata");

    stations["Braga".lower()] = "94-29157";
    stationList.append("Braga");

    stations["Bustelo".lower()] = "94-8334";
    stationList.append("Bustelo");

    stations["Cabanoes".lower()] = "94-42150";
    stationList.append("Cabanoes");

    stations["Cabeda".lower()] = "94-8029";
    stationList.append("Cabeda");

    stations["Cacela".lower()] = "94-73452";
    stationList.append("Cacela");

    stations["Cacia".lower()] = "94-38075";
    stationList.append("Cacia");

    stations["Caide".lower()] = "94-8383";
    stationList.append("Caide");

    stations["Caldas da Rainha".lower()] = "94-63008";
    stationList.append("Caldas da Rainha");

    stations["Caldas de Moledo".lower()] = "94-9399";
    stationList.append("Caldas de Moledo");

    stations["Caminha".lower()] = "94-18242";
    stationList.append("Caminha");

    stations["Canas-Felgueira".lower()] = "94-46599";
    stationList.append("Canas-Felgueira");

    stations["Canelas".lower()] = "94-38117";
    stationList.append("Canelas");

    stations["Canicos".lower()] = "94-28100";
    stationList.append("Canicos");

    stations["Carapecos".lower()] = "94-6197";
    stationList.append("Carapecos");

    stations["Carrascal-Delongo".lower()] = "94-40030";
    stationList.append("Carrascal-Delongo");

    stations["Carreco".lower()] = "94-18085";
    stationList.append("Carreco");

    stations["Carregado".lower()] = "94-31336";
    stationList.append("Carregado");

    stations["Carregal do Sal".lower()] = "94-46482";
    stationList.append("Carregal do Sal");

    stations["Carreira".lower()] = "94-6056";
    stationList.append("Carreira");

    stations["Carvalha".lower()] = "94-18416";
    stationList.append("Carvalha");

    stations["Carvalhal Portela".lower()] = "94-42309";
    stationList.append("Carvalhal Portela");

    stations["Carvalheira-Maceda".lower()] = "94-38356";
    stationList.append("Carvalheira-Maceda");

    stations["Carvalhos de Figueiredo".lower()] = "94-40113";
    stationList.append("Carvalhos de Figueiredo");

    stations["Casa Branca".lower()] = "94-74005";
    stationList.append("Casa Branca");

    stations["Casais".lower()] = "94-35147";
    stationList.append("Casais");

    stations["Casal Alvaro".lower()] = "94-42168";
    stationList.append("Casal Alvaro");

    stations["Castanheira do Ribatejo".lower()] = "94-31310";
    stationList.append("Castanheira do Ribatejo");

    stations["Castelejo".lower()] = "94-46409";
    stationList.append("Castelejo");

    stations["Castelo Branco".lower()] = "94-53009";
    stationList.append("Castelo Branco");

    stations["Castelo Novo".lower()] = "94-53314";
    stationList.append("Castelo Novo");

    stations["Castro Marim".lower()] = "94-73502";
    stationList.append("Castro Marim");

    stations["Cavaco".lower()] = "94-44172";
    stationList.append("Cavaco");

    stations["Caxarias".lower()] = "94-34330";
    stationList.append("Caxarias");

    stations["Celorico da Beira".lower()] = "94-48405";
    stationList.append("Celorico da Beira");

    stations["Cerdeira".lower()] = "94-49205";
    stationList.append("Cerdeira");

    stations["Cete".lower()] = "94-8227";
    stationList.append("Cete");

    stations["Chanca".lower()] = "94-56101";
    stationList.append("Chanca");

    stations["Coimbra".lower()] = "94-41020";
    stationList.append("Coimbra");

    stations["Coimbra-B".lower()] = "94-36004";
    stationList.append("Coimbra-B");

    stations["Coimbroes".lower()] = "94-39149";
    stationList.append("Coimbroes");

    stations["Conceicao".lower()] = "94-73379";
    stationList.append("Conceicao");

    stations["Contumil".lower()] = "94-3004";
    stationList.append("Contumil");

    stations["Cortegaca".lower()] = "94-38372";
    stationList.append("Cortegaca");

    stations["Couto de Cambeses".lower()] = "94-29033";
    stationList.append("Couto de Cambeses");

    stations["Couto de Cucujaes".lower()] = "94-44297";
    stationList.append("Couto de Cucujaes");

    stations["Covas".lower()] = "94-28290";
    stationList.append("Covas");

    stations["Covelinhas".lower()] = "94-10090";
    stationList.append("Covelinhas");

    stations["Covilha".lower()] = "94-54007";
    stationList.append("Covilha");

    stations["Crato".lower()] = "94-56267";
    stationList.append("Crato");

    stations["Cuba".lower()] = "94-74476";
    stationList.append("Cuba");

    stations["Cuca".lower()] = "94-28209";
    stationList.append("Cuca");

    stations["Curia".lower()] = "94-37119";
    stationList.append("Curia");

    stations["Curvaceiras".lower()] = "94-40063";
    stationList.append("Curvaceiras");

    stations["Dagorda-Peniche".lower()] = "94-62802";
    stationList.append("Dagorda-Peniche");

    stations["Darque".lower()] = "94-6387";
    stationList.append("Darque");

    stations["Dois Portos".lower()] = "94-62380";
    stationList.append("Dois Portos");

    stations["Donas".lower()] = "94-53520";
    stationList.append("Donas");

    stations["Durraes".lower()] = "94-6262";
    stationList.append("Durraes");

    stations["Eirol".lower()] = "94-42119";
    stationList.append("Eirol");

    stations["Eixo".lower()] = "94-42077";
    stationList.append("Eixo");

    stations["Elvas".lower()] = "94-57497";
    stationList.append("Elvas");

    stations["Entroncamento".lower()] = "94-34009";
    stationList.append("Entroncamento");

    stations["Ermesinde".lower()] = "94-4002";
    stationList.append("Ermesinde");

    stations["Ermida".lower()] = "94-9258";
    stationList.append("Ermida");

    stations["Ermidas-Sado".lower()] = "94-93005";
    stationList.append("Ermidas-Sado");

    stations["Escapaes".lower()] = "94-44222";
    stationList.append("Escapaes");

    stations["Esgueira".lower()] = "94-42028";
    stationList.append("Esgueira");

    stations["Esmeriz".lower()] = "94-5033";
    stationList.append("Esmeriz");

    stations["Esmoriz".lower()] = "94-38406";
    stationList.append("Esmoriz");

    stations["Espadanal da Azambuja".lower()] = "94-31401";
    stationList.append("Espadanal da Azambuja");

    stations["Espadaneira".lower()] = "94-35162";
    stationList.append("Espadaneira");

    stations["Espinho".lower()] = "94-39008";
    stationList.append("Espinho");

    stations["Espinho-Vouga".lower()] = "94-44016";
    stationList.append("Espinho-Vouga");

    stations["Esqueiro".lower()] = "94-18291";
    stationList.append("Esqueiro");

    stations["Estarreja".lower()] = "94-38158";
    stationList.append("Estarreja");

    stations["Estombar-Lagoa".lower()] = "94-90241";
    stationList.append("Estombar-Lagoa");

    stations["Evora".lower()] = "94-83006";
    stationList.append("Evora");

    stations["Famalicao".lower()] = "94-5074";
    stationList.append("Famalicao");

    stations["Famalicao da Nazare".lower()] = "94-63180";
    stationList.append("Famalicao da Nazare");

    stations["Faria".lower()] = "94-44271";
    stationList.append("Faria");

    stations["Faro".lower()] = "94-73007";
    stationList.append("Faro");

    stations["Fatela-Penamacor".lower()] = "94-53462";
    stationList.append("Fatela-Penamacor");

    stations["Fatima".lower()] = "94-34249";
    stationList.append("Fatima");

    stations["Feliteira".lower()] = "94-62364";
    stationList.append("Feliteira");

    stations["Fernando Po".lower()] = "94-71050";
    stationList.append("Fernando Po");

    stations["Ferradosa".lower()] = "94-11114";
    stationList.append("Ferradosa");

    stations["Ferragudo".lower()] = "94-90274";
    stationList.append("Ferragudo");

    stations["Ferrao".lower()] = "94-10165";
    stationList.append("Ferrao");

    stations["Ferreiros".lower()] = "94-29132";
    stationList.append("Ferreiros");

    stations["Figueira da Foz".lower()] = "94-64113";
    stationList.append("Figueira da Foz");

    stations["Fontela".lower()] = "94-64089";
    stationList.append("Fontela");

    stations["Fontela-A".lower()] = "94-64097";
    stationList.append("Fontela-A");

    stations["Formoselha".lower()] = "94-35030";
    stationList.append("Formoselha");

    stations["Fornos de Algodres".lower()] = "94-48249";
    stationList.append("Fornos de Algodres");

    stations["Francelos".lower()] = "94-39081";
    stationList.append("Francelos");

    stations["Fratel".lower()] = "94-52571";
    stationList.append("Fratel");

    stations["Freineda".lower()] = "94-49387";
    stationList.append("Freineda");

    stations["Freixo de Numao-Mos do Douro".lower()] = "94-11247";
    stationList.append("Freixo de Numao-Mos do Douro");

    stations["Funcheira".lower()] = "94-77008";
    stationList.append("Funcheira");

    stations["Fundao".lower()] = "94-53546";
    stationList.append("Fundao");

    stations["Fungalvaz".lower()] = "94-34199";
    stationList.append("Fungalvaz");

    stations["Fuseta".lower()] = "94-73205";
    stationList.append("Fuseta");

    stations["Fuseta-A".lower()] = "94-73197";
    stationList.append("Fuseta-A");

    stations["Gata".lower()] = "94-49049";
    stationList.append("Gata");

    stations["General Torres".lower()] = "94-39172";
    stationList.append("General Torres");

    stations["Giesteira".lower()] = "94-28159";
    stationList.append("Giesteira");

    stations["Godim".lower()] = "94-9423";
    stationList.append("Godim");

    stations["Gondarem".lower()] = "94-18325";
    stationList.append("Gondarem");

    stations["Gouveia".lower()] = "94-48165";
    stationList.append("Gouveia");

    stations["Grandola".lower()] = "94-92577";
    stationList.append("Grandola");

    stations["Granja".lower()] = "94-39040";
    stationList.append("Granja");

    stations["Guarda".lower()] = "94-49007";
    stationList.append("Guarda");

    stations["Guia".lower()] = "94-63800";
    stationList.append("Guia");

    stations["Guimaraes".lower()] = "94-24000";
    stationList.append("Guimaraes");

    stations["Irivo".lower()] = "94-8243";
    stationList.append("Irivo");

    stations["Jerumelo".lower()] = "94-62257";
    stationList.append("Jerumelo");

    stations["Juncal".lower()] = "94-9050";
    stationList.append("Juncal");

    stations["Lagos".lower()] = "94-90464";
    stationList.append("Lagos");

    stations["Lamarosa".lower()] = "94-34090";
    stationList.append("Lamarosa");

    stations["Lapa".lower()] = "94-44057";
    stationList.append("Lapa");

    stations["Lapa do Lobo".lower()] = "94-46581";
    stationList.append("Lapa do Lobo");

    stations["Lardosa".lower()] = "94-53215";
    stationList.append("Lardosa");

    stations["Lares".lower()] = "94-64055";
    stationList.append("Lares");

    stations["Leandro".lower()] = "94-4036";
    stationList.append("Leandro");

    stations["Leiria".lower()] = "94-63560";
    stationList.append("Leiria");

    stations["Lisboa - Entrecampos".lower()] = "94-66050";
    stationList.append("Lisboa - Entrecampos");

    stations["Lisboa - Oriente".lower()] = "94-31039";
    stationList.append("Lisboa - Oriente");

    stations["Lisboa - Santa Apolonia".lower()] = "94-30007";
    stationList.append("Lisboa - Santa Apolonia");

    stations["Lisboa - Sete Rios".lower()] = "94-66076";
    stationList.append("Lisboa - Sete Rios");

    stations["Litem".lower()] = "94-34504";
    stationList.append("Litem");

    stations["Livracao".lower()] = "94-8474";
    stationList.append("Livracao");

    stations["Livramento".lower()] = "94-73239";
    stationList.append("Livramento");

    stations["Lordelo".lower()] = "94-28191";
    stationList.append("Lordelo");

    stations["Loule".lower()] = "94-78238";
    stationList.append("Loule");

    stations["Lourical".lower()] = "94-63875";
    stationList.append("Lourical");

    stations["Louro".lower()] = "94-5116";
    stationList.append("Louro");

    stations["Lousado".lower()] = "94-5009";
    stationList.append("Lousado");

    stations["Luso-Bucaco".lower()] = "94-46094";
    stationList.append("Luso-Bucaco");

    stations["Luz".lower()] = "94-73262";
    stationList.append("Luz");

    stations["Macinhata".lower()] = "94-42325";
    stationList.append("Macinhata");

    stations["Madalena".lower()] = "94-39123";
    stationList.append("Madalena");

    stations["Mafra".lower()] = "94-62166";
    stationList.append("Mafra");

    stations["Malveira".lower()] = "94-62224";
    stationList.append("Malveira");

    stations["Mangualde".lower()] = "94-48009";
    stationList.append("Mangualde");

    stations["Marco de Canaveses".lower()] = "94-9001";
    stationList.append("Marco de Canaveses");

    stations["Marinha Grande".lower()] = "94-63461";
    stationList.append("Marinha Grande");

    stations["Martinganca-Maceira".lower()] = "94-63404";
    stationList.append("Martinganca-Maceira");

    stations["Marujal".lower()] = "94-65052";
    stationList.append("Marujal");

    stations["Mato de Miranda".lower()] = "94-32383";
    stationList.append("Mato de Miranda");

    stations["Mazagao".lower()] = "94-29116";
    stationList.append("Mazagao");

    stations["Mealhada".lower()] = "94-37051";
    stationList.append("Mealhada");

    stations["Meia Praia".lower()] = "94-90431";
    stationList.append("Meia Praia");

    stations["Meinedo".lower()] = "94-8359";
    stationList.append("Meinedo");

    stations["Messines-Alte".lower()] = "94-77735";
    stationList.append("Messines-Alte");

    stations["Mexilhoeira Grande".lower()] = "94-90381";
    stationList.append("Mexilhoeira Grande");

    stations["Midoes".lower()] = "94-6080";
    stationList.append("Midoes");

    stations["Mira Sintra-Melecas".lower()] = "94-62042";
    stationList.append("Mira Sintra-Melecas");

    stations["Miramar".lower()] = "94-39073";
    stationList.append("Miramar");

    stations["Mirao".lower()] = "94-9225";
    stationList.append("Mirao");

    stations["Miuzela".lower()] = "94-49239";
    stationList.append("Miuzela");

    stations["Mogofores".lower()] = "94-37143";
    stationList.append("Mogofores");

    stations["Moimenta-Alcafache".lower()] = "94-46763";
    stationList.append("Moimenta-Alcafache");

    stations["Moledo do Minho".lower()] = "94-18200";
    stationList.append("Moledo do Minho");

    stations["Monte de Lobos".lower()] = "94-46219";
    stationList.append("Monte de Lobos");

    stations["Monte de Paramos".lower()] = "94-44040";
    stationList.append("Monte de Paramos");

    stations["Monte Gordo".lower()] = "94-73544";
    stationList.append("Monte Gordo");

    stations["Monte Real".lower()] = "94-63685";
    stationList.append("Monte Real");

    stations["Monte Redondo".lower()] = "94-63735";
    stationList.append("Monte Redondo");

    stations["Montemor".lower()] = "94-65029";
    stationList.append("Montemor");

    stations["Mortagua".lower()] = "94-46243";
    stationList.append("Mortagua");

    stations["Moscavide".lower()] = "94-31047";
    stationList.append("Moscavide");

    stations["Mosteiro".lower()] = "94-9134";
    stationList.append("Mosteiro");

    stations["Mouquim".lower()] = "94-5108";
    stationList.append("Mouquim");

    stations["Mourisca Vouga".lower()] = "94-42259";
    stationList.append("Mourisca Vouga");

    stations["Mouriscas-A".lower()] = "94-52167";
    stationList.append("Mouriscas-A");

    stations["Nelas".lower()] = "94-46672";
    stationList.append("Nelas");

    stations["Nespereira".lower()] = "94-28266";
    stationList.append("Nespereira");

    stations["Nine".lower()] = "94-6007";
    stationList.append("Nine");

    stations["Obidos".lower()] = "94-62836";
    stationList.append("Obidos");

    stations["Oia".lower()] = "94-37275";
    stationList.append("Oia");

    stations["Oleiros".lower()] = "94-8250";
    stationList.append("Oleiros");

    stations["Olhao".lower()] = "94-73106";
    stationList.append("Olhao");

    stations["Oliveira".lower()] = "94-8409";
    stationList.append("Oliveira");

    stations["Oliveira de Azemeis".lower()] = "94-44339";
    stationList.append("Oliveira de Azemeis");

    stations["Oliveira do Bairro".lower()] = "94-37218";
    stationList.append("Oliveira do Bairro");

    stations["Oliveirinha-Cabanas".lower()] = "94-46524";
    stationList.append("Oliveirinha-Cabanas");

    stations["Oronhe".lower()] = "94-42176";
    stationList.append("Oronhe");

    stations["Outeiro".lower()] = "94-62612";
    stationList.append("Outeiro");

    stations["Ovar".lower()] = "94-38299";
    stationList.append("Ovar");

    stations["Pacos de Brandao".lower()] = "94-44107";
    stationList.append("Pacos de Brandao");

    stations["Paialvo".lower()] = "94-34157";
    stationList.append("Paialvo");

    stations["Pala".lower()] = "94-9100";
    stationList.append("Pala");

    stations["Pampilhosa".lower()] = "94-37002";
    stationList.append("Pampilhosa");

    stations["Papizios".lower()] = "94-46441";
    stationList.append("Papizios");

    stations["Parada".lower()] = "94-8201";
    stationList.append("Parada");

    stations["Paraimo-Sangalhos".lower()] = "94-37184";
    stationList.append("Paraimo-Sangalhos");

    stations["Paramos".lower()] = "94-38414";
    stationList.append("Paramos");

    stations["Paredes".lower()] = "94-8276";
    stationList.append("Paredes");

    stations["Parque das Cidades".lower()] = "94-78295";
    stationList.append("Parque das Cidades");

    stations["Pataias".lower()] = "94-63354";
    stationList.append("Pataias");

    stations["Paul".lower()] = "94-62745";
    stationList.append("Paul");

    stations["Pedra Furada".lower()] = "94-62133";
    stationList.append("Pedra Furada");

    stations["Pegoes".lower()] = "94-71126";
    stationList.append("Pegoes");

    stations["Pelariga".lower()] = "94-34702";
    stationList.append("Pelariga");

    stations["Penafiel".lower()] = "94-8318";
    stationList.append("Penafiel");

    stations["Pereira".lower()] = "94-35055";
    stationList.append("Pereira");

    stations["Pereirinhas".lower()] = "94-28217";
    stationList.append("Pereirinhas");

    stations["Pero Negro".lower()] = "94-62315";
    stationList.append("Pero Negro");

    stations["Pinhal Novo".lower()] = "94-68007";
    stationList.append("Pinhal Novo");

    stations["Pinhao".lower()] = "94-10249";
    stationList.append("Pinhao");

    stations["Poceirao".lower()] = "94-71001";
    stationList.append("Poceirao");

    stations["Pocinho".lower()] = "94-12005";
    stationList.append("Pocinho");

    stations["Poco Barreto".lower()] = "94-90134";
    stationList.append("Poco Barreto");

    stations["Pombal".lower()] = "94-34645";
    stationList.append("Pombal");

    stations["Ponte de Sor".lower()] = "94-55293";
    stationList.append("Ponte de Sor");

    stations["Porta Nova".lower()] = "94-73338";
    stationList.append("Porta Nova");

    stations["Portalegre".lower()] = "94-57000";
    stationList.append("Portalegre");

    stations["Portela".lower()] = "94-4101";
    stationList.append("Portela");

    stations["Portimao".lower()] = "94-90290";
    stationList.append("Portimao");

    stations["Porto - Campanha".lower()] = "94-2006";
    stationList.append("Porto - Campanha");

    stations["Porto - Sao Bento".lower()] = "94-1008";
    stationList.append("Porto - Sao Bento");

    stations["Porto de Rei".lower()] = "94-9282";
    stationList.append("Porto de Rei");

    stations["Povoa".lower()] = "94-31146";
    stationList.append("Povoa");

    stations["Pragal".lower()] = "94-17087";
    stationList.append("Pragal");

    stations["Praia do Ribatejo".lower()] = "94-51128";
    stationList.append("Praia do Ribatejo");

    stations["Quintans".lower()] = "94-37358";
    stationList.append("Quintans");

    stations["Ramalhal".lower()] = "94-62547";
    stationList.append("Ramalhal");

    stations["Recarei-Sobreira".lower()] = "94-8177";
    stationList.append("Recarei-Sobreira");

    stations["Recesinhos".lower()] = "94-8441";
    stationList.append("Recesinhos");

    stations["Rede".lower()] = "94-9357";
    stationList.append("Rede");

    stations["Regua".lower()] = "94-10009";
    stationList.append("Regua");

    stations["Reguengo-V.Pedra-Pontevel".lower()] = "94-33084";
    stationList.append("Reguengo-V.Pedra-Pontevel");

    stations["Retaxo".lower()] = "94-52845";
    stationList.append("Retaxo");

    stations["Reveles".lower()] = "94-65128";
    stationList.append("Reveles");

    stations["Riachos-T.Novas-Golega".lower()] = "94-32466";
    stationList.append("Riachos-T.Novas-Golega");

    stations["Rio Meao".lower()] = "94-44115";
    stationList.append("Rio Meao");

    stations["Rio Tinto".lower()] = "94-3038";
    stationList.append("Rio Tinto");

    stations["Rochoso".lower()] = "94-49163";
    stationList.append("Rochoso");

    stations["Runa".lower()] = "94-62422";
    stationList.append("Runa");

    stations["Ruílhe".lower()] = "94-29074";
    stationList.append("Ruílhe");

    stations["Sabugo".lower()] = "94-62091";
    stationList.append("Sabugo");

    stations["Sacavem".lower()] = "94-31062";
    stationList.append("Sacavem");

    stations["Salir do Porto".lower()] = "94-63107";
    stationList.append("Salir do Porto");

    stations["Salreu".lower()] = "94-38125";
    stationList.append("Salreu");

    stations["Sampaio-Oleiros".lower()] = "94-44073";
    stationList.append("Sampaio-Oleiros");

    stations["Sanfins".lower()] = "94-44198";
    stationList.append("Sanfins");

    stations["Santa Cita".lower()] = "94-40105";
    stationList.append("Santa Cita");

    stations["Santa Clara-Saboia".lower()] = "94-77388";
    stationList.append("Santa Clara-Saboia");

    stations["Santa Comba Dao".lower()] = "94-46367";
    stationList.append("Santa Comba Dao");

    stations["Santa Eulalia-A".lower()] = "94-57315";
    stationList.append("Santa Eulalia-A");

    stations["Santa Iria".lower()] = "94-31112";
    stationList.append("Santa Iria");

    stations["Santa Margarida".lower()] = "94-51185";
    stationList.append("Santa Margarida");

    stations["Santana-Cartaxo".lower()] = "94-32045";
    stationList.append("Santana-Cartaxo");

    stations["Santarem".lower()] = "94-32185";
    stationList.append("Santarem");

    stations["Santiago de Riba-Ul".lower()] = "94-44313";
    stationList.append("Santiago de Riba-Ul");

    stations["Santo Tirso".lower()] = "94-28068";
    stationList.append("Santo Tirso");

    stations["Sao Frutuoso".lower()] = "94-4051";
    stationList.append("Sao Frutuoso");

    stations["Sao Joao da Madeira".lower()] = "94-44255";
    stationList.append("Sao Joao da Madeira");

    stations["Sao Joao das Craveiras".lower()] = "94-71159";
    stationList.append("Sao Joao das Craveiras");

    stations["Sao Joao de Ver".lower()] = "94-44156";
    stationList.append("Sao Joao de Ver");

    stations["Sao Joao Loure".lower()] = "94-42093";
    stationList.append("Sao Joao Loure");

    stations["Sao Mamede".lower()] = "94-62786";
    stationList.append("Sao Mamede");

    stations["Sao Martinho do Campo".lower()] = "94-8102";
    stationList.append("Sao Martinho do Campo");

    stations["Sao Martinho do Porto".lower()] = "94-63131";
    stationList.append("Sao Martinho do Porto");

    stations["Sao Pedro da Torre".lower()] = "94-18440";
    stationList.append("Sao Pedro da Torre");

    stations["Sao Romao".lower()] = "94-4077";
    stationList.append("Sao Romao");

    stations["Sapataria".lower()] = "94-62299";
    stationList.append("Sapataria");

    stations["Sarnadas".lower()] = "94-52803";
    stationList.append("Sarnadas");

    stations["Seica-Ourem".lower()] = "94-34264";
    stationList.append("Seica-Ourem");

    stations["Seixas".lower()] = "94-18275";
    stationList.append("Seixas");

    stations["Senhora da Agonia".lower()] = "94-18234";
    stationList.append("Senhora da Agonia");

    stations["Senhora das Neves".lower()] = "94-6312";
    stationList.append("Senhora das Neves");

    stations["Sernada do Vouga".lower()] = "94-43000";
    stationList.append("Sernada do Vouga");

    stations["Setil".lower()] = "94-32003";
    stationList.append("Setil");

    stations["Silva".lower()] = "94-6155";
    stationList.append("Silva");

    stations["Silvalde".lower()] = "94-38422";
    stationList.append("Silvalde");

    stations["Silvalde-Vouga".lower()] = "94-44032";
    stationList.append("Silvalde-Vouga");

    stations["Silves".lower()] = "94-90183";
    stationList.append("Silves");

    stations["Simoes".lower()] = "94-34744";
    stationList.append("Simoes");

    stations["Soalheira".lower()] = "94-53264";
    stationList.append("Soalheira");

    stations["Soito".lower()] = "94-46185";
    stationList.append("Soito");

    stations["Soudos-Vila Nova".lower()] = "94-40014";
    stationList.append("Soudos-Vila Nova");

    stations["Soure".lower()] = "94-34801";
    stationList.append("Soure");

    stations["Souselas".lower()] = "94-36087";
    stationList.append("Souselas");

    stations["Suzao".lower()] = "94-8060";
    stationList.append("Suzao");

    stations["Tadim".lower()] = "94-29090";
    stationList.append("Tadim");

    stations["Taipa-Requeixo".lower()] = "94-42127";
    stationList.append("Taipa-Requeixo");

    stations["Tamel".lower()] = "94-6213";
    stationList.append("Tamel");

    stations["Tancos".lower()] = "94-51086";
    stationList.append("Tancos");

    stations["Taveiro".lower()] = "94-35139";
    stationList.append("Taveiro");

    stations["Tavira".lower()] = "94-73320";
    stationList.append("Tavira");

    stations["Telhal".lower()] = "94-62067";
    stationList.append("Telhal");

    stations["Terronhas".lower()] = "94-8136";
    stationList.append("Terronhas");

    stations["Tojeirinha".lower()] = "94-52738";
    stationList.append("Tojeirinha");

    stations["Tomar".lower()] = "94-40154";
    stationList.append("Tomar");

    stations["Torre das Vargens".lower()] = "94-56002";
    stationList.append("Torre das Vargens");

    stations["Torres Vedras".lower()] = "94-62471";
    stationList.append("Torres Vedras");

    stations["Tortosendo".lower()] = "94-53678";
    stationList.append("Tortosendo");

    stations["Tramagal".lower()] = "94-51243";
    stationList.append("Tramagal");

    stations["Trancoso".lower()] = "94-8151";
    stationList.append("Trancoso");

    stations["Travagem".lower()] = "94-4010";
    stationList.append("Travagem");

    stations["Travasso".lower()] = "94-42135";
    stationList.append("Travasso");

    stations["Trofa".lower()] = "94-4630";
    stationList.append("Trofa");

    stations["Tua".lower()] = "94-11007";
    stationList.append("Tua");

    stations["Tunes".lower()] = "94-78006";
    stationList.append("Tunes");

    stations["Vacarica".lower()] = "94-46045";
    stationList.append("Vacarica");

    stations["Valadares".lower()] = "94-39115";
    stationList.append("Valadares");

    stations["Valado".lower()] = "94-63263";
    stationList.append("Valado");

    stations["Vale de Figueira".lower()] = "94-32284";
    stationList.append("Vale de Figueira");

    stations["Vale de Prazeres".lower()] = "94-53397";
    stationList.append("Vale de Prazeres");

    stations["Vale de Santarem".lower()] = "94-32102";
    stationList.append("Vale de Santarem");

    stations["Valega".lower()] = "94-38240";
    stationList.append("Valega");

    stations["Valenca".lower()] = "94-7005";
    stationList.append("Valenca");

    stations["Valongo".lower()] = "94-8086";
    stationList.append("Valongo");

    stations["Valongo Vouga".lower()] = "94-42291";
    stationList.append("Valongo Vouga");

    stations["Vargelas".lower()] = "94-11148";
    stationList.append("Vargelas");

    stations["Vendas Novas".lower()] = "94-72009";
    stationList.append("Vendas Novas");

    stations["Vermoil".lower()] = "94-34553";
    stationList.append("Vermoil");

    stations["Verride".lower()] = "94-65086";
    stationList.append("Verride");

    stations["Vesuvio".lower()] = "94-11197";
    stationList.append("Vesuvio");

    stations["Viana do Castelo".lower()] = "94-18002";
    stationList.append("Viana do Castelo");

    stations["Vila da Feira".lower()] = "94-44206";
    stationList.append("Vila da Feira");

    stations["Vila das Aves".lower()] = "94-28134";
    stationList.append("Vila das Aves");

    stations["Vila Fernando".lower()] = "94-49114";
    stationList.append("Vila Fernando");

    stations["Vila Franca das Naves".lower()] = "94-48546";
    stationList.append("Vila Franca das Naves");

    stations["Vila Franca de Xira".lower()] = "94-31278";
    stationList.append("Vila Franca de Xira");

    stations["Vila Mea".lower()] = "94-8433";
    stationList.append("Vila Mea");

    stations["Vila Nova da Baronia".lower()] = "94-74278";
    stationList.append("Vila Nova da Baronia");

    stations["Vila Nova da Rainha".lower()] = "94-31377";
    stationList.append("Vila Nova da Rainha");

    stations["Vila Nova de Ancos".lower()] = "94-34868";
    stationList.append("Vila Nova de Ancos");

    stations["Vila Nova de Cerveira".lower()] = "94-18341";
    stationList.append("Vila Nova de Cerveira");

    stations["Vila Nova de Gaia-Devesas".lower()] = "94-39164";
    stationList.append("Vila Nova de Gaia-Devesas");

    stations["Vila Pouca do Campo".lower()] = "94-35105";
    stationList.append("Vila Pouca do Campo");

    stations["Vila Real de Santo Antonio".lower()] = "94-73569";
    stationList.append("Vila Real de Santo Antonio");

    stations["Vila Velha de Rodao".lower()] = "94-52647";
    stationList.append("Vila Velha de Rodao");

    stations["Vilar Formoso".lower()] = "94-49460";
    stationList.append("Vilar Formoso");

    stations["Vilela-Fornos".lower()] = "94-36053";
    stationList.append("Vilela-Fornos");

    stations["Virtudes".lower()] = "94-33043";
    stationList.append("Virtudes");

    stations["Vizela".lower()] = "94-28233";
    stationList.append("Vizela");

    stations["Zibreira".lower()] = "94-62331";
    stationList.append("Zibreira");

def getStation(station_name):
    result = ['-','-']
    station_name = station_name.lower()
    station_name = station_name.replace(' ','-')
    station_keys = station_name.split('-')
    initStations()

    for station in stationList:
        compare_station = str(station).lower()
        compare_station = compare_station.replace('-',' ')
        compare_station = compare_station.split(' ')

        is_match = True
        for key in station_keys:
            if key not in compare_station:
                is_match = False

        if(is_match):
            result[0] = str(station)
            result[1] = stations[str(station).lower()] 
            return result

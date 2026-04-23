
  ⚠️  DANGEROUS COMMAND: Security scan — [HIGH] Insecure TLS flag detected: Flag '-k' disables TLS certificate verification, allowing MITM attacks
      curl -k -L 'https://kt.gov.lt/lt/naujienos/orion-asset-management-gales-vykdyti-sandori' | head -n 120

      [o]nce  |  [s]ession  |  [d]eny

      Choice [o/s/D]: 
      ⏱ Timeout - denying command

  ┊ review diff
a/JOBLOG.md → b/JOBLOG.md
@@ -0,0 +1,70 @@
+Admen research notes
+
+Scope
+- Prepared public-source dossier in Lithuanian for Klaipėdos LEZ account-management use.
+- Focused on last 5 years, practical meeting-readiness, selective facts.
+
+Identity / structure
+- Official website: admen.lt presents “Admen” as signage / LED / custom advertising production company in Klaipėda, export-oriented, claims 30+ years of experience.
+- Okredo page for UAB "ADMEN" (code 300860736) aligns with Klaipėda, Pramonės g. 8A, 169 employees, 2024 turnover EUR 11.51m, director Ruslanas Aleksandravičius.
+- Official website contact page currently shows company code 302944948, which belongs to UAB "ADMEN BALTIC". This suggests public-facing brand / group structure is not fully cleanly separated online.
+- UAB "ADMEN BALTIC" also exists in public data, linked to advertising activity, Kaunas reg. address, 2024 turnover EUR 4.37m, but only 1 employee in Sodra according to Okredo. Good meeting question: how are Admen / Admen Baltic roles split?
+
+Main facts collected
+- Oaklins: in 2020-08, private owners sold 44% stake in Admen to Orion Private Equity, including 4% new capital.
+- Official ES support page:
+  - COVID products manufacturing project: 2021-02-22 to 2021-04-08, total EUR 129,260, EU funded EUR 122,797.
+  - E-commerce model deployment: 2022-02-28 to 2023-02-11, EU support EUR 21,450.
+  - Environmentally friendly product implementation: 2023-07 to 2024-07, total EUR 60,302, EU support EUR 50,000.
+  - Employee skills project no. 02-035-K-0316: 2024-07-30 to 2026-07-30, total EUR 106,251, EU funds EUR 63,750.60.
+- Sustainability page:
+  - Factory on 100% renewable electricity since 2023.
+  - Claims >75% annual CO2e reduction and ~78% reduction per revenue unit after switch.
+  - Uses powder coating on ~80% of products; promotes recycled acrylic and FSC wood sourcing.
+- Okredo UAB ADMEN:
+  - 2024 turnover EUR 11,511,143 (+4%).
+  - 2024 net profit / gross profit shown EUR 1,350,909 (+5%).
+  - 169 employees (+33 y/y) and avg wage EUR 2,831.19.
+  - Pre-Score A, no registered debts at access time.
+  - Equity EUR 1.639m (-8%), liabilities EUR 1.760m (+97%), current assets EUR 3.166m (+32%).
+- Okredo procurement traces for UAB ADMEN:
+  - wonProcurements past year: 3, total EUR 5,837.
+  - 2025-06-26 Nidos kultūros ir turizmo informacijos centras, lauko reklamos iškaba, EUR 4,446.
+  - 2025-07-24 Inovacijų agentūra, garso ir vaizdo aparatūros priedai, EUR 121.
+  - 2026-01-26 Prienų r. savivaldybės administracija, reklaminės neoninės lempos, EUR 1,270. (not used in timeline if restricting to last 5 years ending now, but visible)
+- Tenderfy for UAB ADMEN BALTIC shows multiple 2024 public contracts, e.g.:
+  - 2024-06-17 Marijampolės futbolo klubas LED ekranas with OS/software/installation EUR 34,848.
+  - 2024-08-13 Kauno technikos kolegija several signage contracts EUR 16,999 / 8,107 / 10,648.
+  - 2023-12-13 Busturas electronic timetables with installation EUR 55,539.
+- BSMA member page says main activity is export; services across EU and further East.
+
+Media / PR traces
+- VŽ article 2024-02-21: “Ne pelenės istorija...” about growth from small hangar to Mercedes-Benz / Hitachi clients; CEO quoted.
+- VŽ article 2024-10-07 included Admen in marketing sector leaders coverage.
+- VŽ article 2024-01-10 about missing cargo / Swiss reputation / fairness fight is associated to Admen in Okredo media feed; details should be treated cautiously because full article is paywalled.
+- Overall media footprint appears modest and selective rather than broad.
+
+Likely meeting sensitivities / questions
+- Clarify legal-entity structure: UAB Admen vs UAB Admen Baltic.
+- How ownership and governance evolved after Orion PE investment.
+- Export market mix today (Nordics / CEE / East?) and exposure to weaker EU demand.
+- Margin management: revenue grew in 2024, but balance-sheet liabilities increased materially.
+- Sustainability claims: how much is customer-driven vs internal efficiency.
+- Public procurement is present but not dominant for UAB Admen; ask whether public sector is strategic or opportunistic.
+
+Sources used
+- https://admen.lt/
+- https://admen.lt/apie-mus/
+- https://admen.lt/tvarumas/
+- https://admen.lt/es-parama/
+- https://admen.lt/kontaktai/
+- https://okredo.com/lt-lt/imone/uab-admen-300860736
+- https://okredo.com/en-lt/company/uab-admen-300860736
+- https://okredo.com/en-lt/company/uab-admen-baltic-302944948
+- https://rekvizitai.vz.lt/imone/admen/
+- https://rekvizitai.vz.lt/imone/admen_baltic/
+- https://www.oaklins.com/baltics/en/deals/106261/
+- https://bsma.lt/en/member/admen/
+- https://www.tenderfy.lt/lt/imone/302944948/uab_admen_baltic
+- https://www.vz.lt/smulkusis-verslas/2024/02/21/ne-pelenes-istorija-is-reklamos-gamybos-300-kv-m-angare-iki-mercedes-benz-ir-hitachi-klientu
+- https://www.vz.lt/rinkodara/2024/10/07/rinkodaros-sektoriaus-lyderiai-apie-sekmes-rakta-ir-fenomenalu-laikmeti-lietuvoje

╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
    ## Admen
    
    ### 1. General points
    - **Eksporto gamintojas**
      Admen viešai save pozicionuoja kaip reklamos konstrukcijų, LED ekranų ir nestandartinių ženklinimo sprendimų gamintoją, dirbantį daugiausia eksporto rinkoms. Oficialioje svetainėje ir BSMA profilyje pabrėžiama veikla visoje ES ir už jos rytinėje kryptimi.
    
    - **Privataus kapitalo etapas**
      2020 m. „Oaklins“ paskelbė, kad privatūs savininkai pardavė 44% „Admen“ akcijų „Orion Private Equity“, iš jų 4% buvo naujai išleistas kapitalas. Tai rodo ne tik savininkų pasikeitimą, bet ir kapitalo įliejimą augimui.
    
    - **Auga su investicijomis**
      Per 2021-2026 m. viešai matoma kelių ES finansuotų projektų seka: COVID produktų gamyba, e. komercijos diegimas, aplinkai palankaus produkto kūrimas ir darbuotojų įgūdžių stiprinimas. Tai labiau primena nuoseklią modernizaciją nei vienkartinę paramos paiešką.
    
    - **Struktūros neaiškumas**
      Viešuose šaltiniuose matyti bent dvi susijusios įmonės: UAB „Admen“ (Klaipėda, kodas 300860736) ir UAB „Admen Baltic“ (kodas 302944948). Oficiali svetainė ne visur aiškiai atskiria, kuri juridinė įmonė vykdo kurią veiklą, todėl susitikime verta tai pasitikslinti.
    
    ### 2. Timeline of key events
    - `2020-08`
      **Orion įėjimas**
      „Oaklins“ paskelbė, kad privatūs „Admen“ savininkai pardavė 44% bendrovės „Orion Private Equity“, įskaitant 4% naujai išleisto kapitalo. Tai svarbiausias viešai matomas nuosavybės pokytis per nagrinėjamą laikotarpį.
    
    - `2021-02`
      **COVID produktų projektas**
      Admen pradėjo ES finansuotą projektą COVID-19 produktų gamybai: apsauginių skydų, pertvarų, bekontakčių matavimo ir srautų valdymo sprendimų. Bendra vertė buvo 129,260 Eur, iš jų 122,797 Eur ES lėšos.
    
    - `2021-04`
      **Greita adaptacija**
      COVID projekto pabaiga jau 2021-04 rodo greitą reagavimą į krizės paklausą ir gamybos lankstumą. Tokie projektai paprastai yra trumpi, bet geri indikatorių, kaip įmonė persijungia į naujus gaminius.
    
    - `2022-02`
      **E. komercijos diegimas**
      Pradėtas e. komercijos modelio projektas, skirtas klientų ir partnerių savitarnai bei vidinių procesų automatizavimui. Tai rodo ne tik pardavimo kanalų, bet ir procesų skaitmeninimo kryptį.
    
    - `2023-02`
      **Skaitmenizavimo užbaigimas**
      Oficialiai baigtas e. komercijos projektas, kuriam skirta 21,450 Eur ES parama. Praktine prasme tai signalizuoja, kad bendrovė investavo į pardavimo ir aptarnavimo infrastruktūrą po pandemijos laikotarpio.
    
    - `2023-07`
      **Žalio produkto projektas**
      Startavo aplinkai palankaus produkto diegimo projektas, orientuotas į medžiagų ir energijos sąnaudų mažinimą. Projekto vertė 60,302 Eur, iš jų 50,000 Eur finansuota pagal „Naujos kartos Lietuva“ priemonę.
    
    - `2023-01`
      **Žalioji elektra**
      Bendrovė skelbia, kad nuo 2023 m. jos gamykla 100% aprūpinama elektra iš atsinaujinančių šaltinių. Taip pat teigiama, kad dėl to CO2e sumažintas daugiau kaip 75%; tai yra pačios įmonės skelbiami rodikliai.
    
    - `2024-02`
      **Matomumas VŽ**
      „Verslo žinios“ publikavo išsamesnį pasakojimą apie Admen kelią nuo mažos gamybos bazės iki darbo su žinomais tarptautiniais prekių ženklais, tarp jų „Mercedes-Benz“ ir „Hitachi“. Tai svarbu reputaciškai: bendrovė pasirodo ne tik kataloguose, bet ir verslo žiniasklaidoje.
    
    - `2024-07`
      **Kompetencijų investicija**
      Pradėtas darbuotojų įgūdžių projektas Nr. 02-035-K-0316, trunkantis iki 2026-07-30. Bendra vertė 106,251 Eur, ES dalis 63,750.60 Eur; tai rodo, kad žmonių kompetencijos laikomos siauruoju augimo tašku.
    
    - `2024-12`
      **Apyvarta virš 11,5 mln.**
      Okredo duomenimis, UAB „Admen“ 2024 m. pasiekė 11.51 mln. Eur apyvartą, 1.35 mln. Eur grynąjį pelną ir 169 darbuotojus. Tai patvirtina, kad bendrovė jau yra vidutinio masto gamybinis žaidėjas, o ne nišinė maža dirbtuvė.
    
    ### 3. Okredo stats
    - **Mastelis**
      Vieši Okredo duomenys UAB „Admen“ rodo jau gana solidų pramoninio B2B gamintojo mastelį. 2024 m. apyvarta siekė 11,511,143 Eur, t. y. apie 4% daugiau nei 2023 m.
    
      Detalės: 2023 m. apyvarta 11,057,863 Eur; 2022 m. 9,400,849 Eur. Tai rodo ne sprogstamą, bet nuoseklų augimą.
    
    - **Pelningumas**
      2024 m. Okredo nurodo 1,350,909 Eur pelną prieš mokesčius ir tokio pat dydžio grynąjį pelną, apie 11.74% grynojo pelningumo. Pelno eilutė augo apie 5% per metus.
    
      Detalės: pelnas prieš mokesčius 2023 m. buvo 1,291,416 Eur, 2022 m. 1,012,730 Eur. Bendras pelningumas 2024 m. sumažėjo iki 27.43%, nors grynasis pelningumas išliko gana aukštas.
    
    - **Darbuotojai**
      Okredo prie UAB „Admen“ rodo 169 darbuotojus ir 2,831.19 Eur vidutinį darbo užmokestį. Darbuotojų skaičius per metus padidėjo 33.
    
      Detalės: pardavimai vienam darbuotojui 2024 m. sudarė 89,227 Eur, pelnas vienam darbuotojui 10,471 Eur. Tai labiau primena veikiančią gamybinę organizaciją su realia darbo jėga nei prekybinį tarpininką.
    
    - **Rizika ir balansas**
      Okredo „Pre-Score“ UAB „Admen“ yra A, t. y. aukščiausio patikimumo lygio signalas pagal jų modelį. Tuo pačiu 2024 m. įsipareigojimai augo sparčiai, todėl vien pozityvaus reitingo nepakanka.
    
      Detalės: nuosavas kapitalas 2024 m. siekė 1,639,418 Eur (-8%), mokėtinos sumos ir įsipareigojimai 1,759,823 Eur (+97%), trumpalaikis turtas 3,165,557 Eur (+32%). Registruotų skolų Okredo prieigos metu nerodyta.
    
    ### 4. Business direction and reputation
    Admen kryptis atrodo gana aiški: eksportuojantis gamintojas, stiprinantis projektinę gamybą, skaitmenizaciją ir „green manufacturing“ pasakojimą. Multikalbė svetainė, BSMA profilis ir vieši projektai leidžia manyti, kad įmonė orientuojasi į tarptautinius B2B klientus, kuriems svarbūs terminai, inžinerinis išpildymas ir gamybos lankstumas.
    
    Reputaciškai tonas labiau santūrus nei triukšmingas. Bendrovė nėra itin plačiai matoma bendrojoje žiniasklaidoje, bet pasirodo verslo ir sektoriaus kontekste, ypač per „Verslo žinias“ ir asociacinę aplinką. Tai reiškia, kad susitikime tikėtinas pragmatiškas, ne PR stiliaus pokalbis.
    
    Praktinė jautri vieta yra grupės struktūra. UAB „Admen“ vieši duomenys rodo Klaipėdos gamyklą ir didelį darbuotojų skaičių, o svetainės kontaktuose nurodomas UAB „Admen Baltic“ kodas. Jei LEZ pokalbyje bus kalbama apie investicijas, plėtrą, NT ar eksporto planus, verta anksti pasitikslinti, kuri įmonė yra gamybinė platforma, kuri - komercinė ar projektinė.
    
    ### 5. Financial situation and past issues
    Bendra finansinė padėtis iš viešų duomenų atrodo stabili. 2022-2024 m. matomas augantis pardavimų lygis, pelningumas išlieka teigiamas, o Okredo patikimumo signalas yra aukštas. Taip pat viešai nematyti registruotų skolų.
    
    Vis dėlto 2024 m. balanse matyti spartus įsipareigojimų augimas. Tai nebūtinai blogas ženklas, nes gali būti susiję su augimu, apyvartinio kapitalo poreikiu ar projektais, tačiau pokalbyje verta suprasti, ar tai buvo sąmoningas finansavimo etapas, ar spaudimas darbo kapitalui.
    
    Papildomas niuansas - vieši duomenys apie UAB „Admen Baltic“ atrodo daug silpnesni pagal darbuotojų skaičių ir patikimumo signalą nei UAB „Admen“. Jei grupė realiai veikia per kelias juridines įmones, vienos įmonės finansiniai rodikliai nebūtinai pilnai atspindi operacinį paveikslą.
    
    ### 6. Legal situation and past issues
    Reikšmingų ilgalaikių ar sisteminių teisinių problemų atviroje paieškoje neradau. Okredo prie UAB „Admen“ nerodė registruotų skolų, o tai yra teigiamas bazinis signalas.
    
    Vienas reikšmingesnis viešas pėdsakas - 2024-01 „Verslo žinių“ publikacija apie dingusio ir pavėluoto krovinio ginčą, žalą reputacijai Šveicarijoje ir ginčą su vežėju. Okredo šią publikaciją priskiria Admen, tačiau pilnas tekstas mokamas, todėl be papildomo teismo bylos patikrinimo nereikėtų kategoriškai teigti bylos baigties ar masto.
    
    Rutininio žemo signalo pėdsakai yra viešųjų pirkimų ir komercinės veiklos dokumentinis fonas. Kol kas tai neatrodo kaip aukštos rizikos teisinė istorija, bet logistikos grandinės ir tarptautinio pristatymo kokybė įmonei akivaizdžiai jautri tema.
    
    ### 7. PR situation and past issues
    PR profilis yra santūrus ir orientuotas į reputaciją per darbus, ne per triukšmingas kampanijas. Pagrindiniai vieši naratyvai: ilgametė patirtis, eksportas, technologinė gamyba, tvarumas ir kokybė.
    
    Viešojoje komunikacijoje ryškus „premium klientų“ ir tarptautinių projektų akcentas. Tai gali reikšti, kad vadovybei svarbi kompetentingo, patikimo, „ne pigiausio tiekėjo“ pozicija.
    
    Potenciali reputacinė jautrybė - pažadai apie tvarumą ir efektyvumą. Bendrovė komunikuoja 100% žaliąją elektrą, CO2 mažinimą ir perdirbtas medžiagas; tokiuose susitikimuose verta kalbėti konkrečiai, nes per daug bendri klausimai gali skambėti paviršutiniškai. Kita jautri tema - logistikos ir terminų laikymasis, turint omenyje minėtą krovinio ginčo istoriją.
    
    ### 8. SWOT
    - `Stiprybės` Eksporto orientacija, reali gamybinė bazė Klaipėdoje, nuoseklus investavimas į technologijas ir darbuotojų kompetencijas, geri 2024 m. mastelio bei pelningumo rodikliai.
    - `Silpnybės` Ne iki galo aiški vieša grupės/juridinių asmenų struktūra, ribotas atviras informacijos kiekis apie akcininkų ir valdymo pokyčius po „Orion“ investicijos, augę įsipareigojimai 2024 m.
    - `Galimybės` Tolimesnė eksporto plėtra, didesnė aukštesnės vertės ženklinimo ir ekranų projektų dalis, LEZ aplinkoje svarbi tvarios gamybos ir operacinio efektyvumo tema.
    - `Grėsmės` Tarptautinės paklausos svyravimai, projektinės gamybos maržų spaudimas, logistikos ir pristatymo kokybės rizika, reputacinė žala, jei tvarumo ar terminų pažadai neatitiktų kliento patirties.
    
    #### Sources
    - https://admen.lt/
    - https://admen.lt/apie-mus/
    - https://admen.lt/tvarumas/
    - https://admen.lt/es-parama/
    - https://admen.lt/kontaktai/
    - https://okredo.com/en-lt/company/uab-admen-300860736
    - https://okredo.com/lt-lt/imone/uab-admen-300860736
    - https://okredo.com/en-lt/company/uab-admen-baltic-302944948
    - https://rekvizitai.vz.lt/imone/admen/
    - https://rekvizitai.vz.lt/imone/admen_baltic/
    - https://www.oaklins.com/baltics/en/deals/106261/
    - https://bsma.lt/en/member/admen/
    - https://www.tenderfy.lt/lt/imone/302944948/uab_admen_baltic
    - https://www.vz.lt/smulkusis-verslas/2024/02/21/ne-pelenes-istorija-is-reklamos-gamybos-300-kv-m-angare-iki-mercedes-benz-ir-hitachi-klientu
## Admen

### 1. General points
- **Eksporto gamintojas**
  Admen viešai save pozicionuoja kaip reklamos konstrukcijų, LED ekranų ir nestandartinių ženklinimo sprendimų gamintoją, dirbantį daugiausia eksporto rinkoms. Oficialioje svetainėje ir BSMA profilyje pabrėžiama veikla visoje ES ir už jos rytinėje kryptimi.

- **Privataus kapitalo etapas**
  2020 m. „Oaklins“ paskelbė, kad privatūs savininkai pardavė 44% „Admen“ akcijų „Orion Private Equity“, iš jų 4% buvo naujai išleistas kapitalas. Tai rodo ne tik savininkų pasikeitimą, bet ir kapitalo įliejimą augimui.

- **Auga su investicijomis**
  Per 2021-2026 m. viešai matoma kelių ES finansuotų projektų seka: COVID produktų gamyba, e. komercijos diegimas, aplinkai palankaus produkto kūrimas ir darbuotojų įgūdžių stiprinimas. Tai labiau primena nuoseklią modernizaciją nei vienkartinę paramos paiešką.

- **Struktūros neaiškumas**
  Viešuose šaltiniuose matyti bent dvi susijusios įmonės: UAB „Admen“ (Klaipėda, kodas 300860736) ir UAB „Admen Baltic“ (kodas 302944948). Oficiali svetainė ne visur aiškiai atskiria, kuri juridinė įmonė vykdo kurią veiklą, todėl susitikime verta tai pasitikslinti.

### 2. Timeline of key events
- `2020-08`
  **Orion įėjimas**
  „Oaklins“ paskelbė, kad privatūs „Admen“ savininkai pardavė 44% bendrovės „Orion Private Equity“, įskaitant 4% naujai išleisto kapitalo. Tai svarbiausias viešai matomas nuosavybės pokytis per nagrinėjamą laikotarpį.

- `2021-02`
  **COVID produktų projektas**
  Admen pradėjo ES finansuotą projektą COVID-19 produktų gamybai: apsauginių skydų, pertvarų, bekontakčių matavimo ir srautų valdymo sprendimų. Bendra vertė buvo 129,260 Eur, iš jų 122,797 Eur ES lėšos.

- `2021-04`
  **Greita adaptacija**
  COVID projekto pabaiga jau 2021-04 rodo greitą reagavimą į krizės paklausą ir gamybos lankstumą. Tokie projektai paprastai yra trumpi, bet geri indikatorių, kaip įmonė persijungia į naujus gaminius.

- `2022-02`
  **E. komercijos diegimas**
  Pradėtas e. komercijos modelio projektas, skirtas klientų ir partnerių savitarnai bei vidinių procesų automatizavimui. Tai rodo ne tik pardavimo kanalų, bet ir procesų skaitmeninimo kryptį.

- `2023-02`
  **Skaitmenizavimo užbaigimas**
  Oficialiai baigtas e. komercijos projektas, kuriam skirta 21,450 Eur ES parama. Praktine prasme tai signalizuoja, kad bendrovė investavo į pardavimo ir aptarnavimo infrastruktūrą po pandemijos laikotarpio.

- `2023-07`
  **Žalio produkto projektas**
  Startavo aplinkai palankaus produkto diegimo projektas, orientuotas į medžiagų ir energijos sąnaudų mažinimą. Projekto vertė 60,302 Eur, iš jų 50,000 Eur finansuota pagal „Naujos kartos Lietuva“ priemonę.

- `2023-01`
  **Žalioji elektra**
  Bendrovė skelbia, kad nuo 2023 m. jos gamykla 100% aprūpinama elektra iš atsinaujinančių šaltinių. Taip pat teigiama, kad dėl to CO2e sumažintas daugiau kaip 75%; tai yra pačios įmonės skelbiami rodikliai.

- `2024-02`
  **Matomumas VŽ**
  „Verslo žinios“ publikavo išsamesnį pasakojimą apie Admen kelią nuo mažos gamybos bazės iki darbo su žinomais tarptautiniais prekių ženklais, tarp jų „Mercedes-Benz“ ir „Hitachi“. Tai svarbu reputaciškai: bendrovė pasirodo ne tik kataloguose, bet ir verslo žiniasklaidoje.

- `2024-07`
  **Kompetencijų investicija**
  Pradėtas darbuotojų įgūdžių projektas Nr. 02-035-K-0316, trunkantis iki 2026-07-30. Bendra vertė 106,251 Eur, ES dalis 63,750.60 Eur; tai rodo, kad žmonių kompetencijos laikomos siauruoju augimo tašku.

- `2024-12`
  **Apyvarta virš 11,5 mln.**
  Okredo duomenimis, UAB „Admen“ 2024 m. pasiekė 11.51 mln. Eur apyvartą, 1.35 mln. Eur grynąjį pelną ir 169 darbuotojus. Tai patvirtina, kad bendrovė jau yra vidutinio masto gamybinis žaidėjas, o ne nišinė maža dirbtuvė.

### 3. Okredo stats
- **Mastelis**
  Vieši Okredo duomenys UAB „Admen“ rodo jau gana solidų pramoninio B2B gamintojo mastelį. 2024 m. apyvarta siekė 11,511,143 Eur, t. y. apie 4% daugiau nei 2023 m.

  Detalės: 2023 m. apyvarta 11,057,863 Eur; 2022 m. 9,400,849 Eur. Tai rodo ne sprogstamą, bet nuoseklų augimą.

- **Pelningumas**
  2024 m. Okredo nurodo 1,350,909 Eur pelną prieš mokesčius ir tokio pat dydžio grynąjį pelną, apie 11.74% grynojo pelningumo. Pelno eilutė augo apie 5% per metus.

  Detalės: pelnas prieš mokesčius 2023 m. buvo 1,291,416 Eur, 2022 m. 1,012,730 Eur. Bendras pelningumas 2024 m. sumažėjo iki 27.43%, nors grynasis pelningumas išliko gana aukštas.

- **Darbuotojai**
  Okredo prie UAB „Admen“ rodo 169 darbuotojus ir 2,831.19 Eur vidutinį darbo užmokestį. Darbuotojų skaičius per metus padidėjo 33.

  Detalės: pardavimai vienam darbuotojui 2024 m. sudarė 89,227 Eur, pelnas vienam darbuotojui 10,471 Eur. Tai labiau primena veikiančią gamybinę organizaciją su realia darbo jėga nei prekybinį tarpininką.

- **Rizika ir balansas**
  Okredo „Pre-Score“ UAB „Admen“ yra A, t. y. aukščiausio patikimumo lygio signalas pagal jų modelį. Tuo pačiu 2024 m. įsipareigojimai augo sparčiai, todėl vien pozityvaus reitingo nepakanka.

  Detalės: nuosavas kapitalas 2024 m. siekė 1,639,418 Eur (-8%), mokėtinos sumos ir įsipareigojimai 1,759,823 Eur (+97%), trumpalaikis turtas 3,165,557 Eur (+32%). Registruotų skolų Okredo prieigos metu nerodyta.

### 4. Business direction and reputation
Admen kryptis atrodo gana aiški: eksportuojantis gamintojas, stiprinantis projektinę gamybą, skaitmenizaciją ir „green manufacturing“ pasakojimą. Multikalbė svetainė, BSMA profilis ir vieši projektai leidžia manyti, kad įmonė orientuojasi į tarptautinius B2B klientus, kuriems svarbūs terminai, inžinerinis išpildymas ir gamybos lankstumas.

Reputaciškai tonas labiau santūrus nei triukšmingas. Bendrovė nėra itin plačiai matoma bendrojoje žiniasklaidoje, bet pasirodo verslo ir sektoriaus kontekste, ypač per „Verslo žinias“ ir asociacinę aplinką. Tai reiškia, kad susitikime tikėtinas pragmatiškas, ne PR stiliaus pokalbis.

Praktinė jautri vieta yra grupės struktūra. UAB „Admen“ vieši duomenys rodo Klaipėdos gamyklą ir didelį darbuotojų skaičių, o svetainės kontaktuose nurodomas UAB „Admen Baltic“ kodas. Jei LEZ pokalbyje bus kalbama apie investicijas, plėtrą, NT ar eksporto planus, verta anksti pasitikslinti, kuri įmonė yra gamybinė platforma, kuri - komercinė ar projektinė.

### 5. Financial situation and past issues
Bendra finansinė padėtis iš viešų duomenų atrodo stabili. 2022-2024 m. matomas augantis pardavimų lygis, pelningumas išlieka teigiamas, o Okredo patikimumo signalas yra aukštas. Taip pat viešai nematyti registruotų skolų.

Vis dėlto 2024 m. balanse matyti spartus įsipareigojimų augimas. Tai nebūtinai blogas ženklas, nes gali būti susiję su augimu, apyvartinio kapitalo poreikiu ar projektais, tačiau pokalbyje verta suprasti, ar tai buvo sąmoningas finansavimo etapas, ar spaudimas darbo kapitalui.

Papildomas niuansas - vieši duomenys apie UAB „Admen Baltic“ atrodo daug silpnesni pagal darbuotojų skaičių ir patikimumo signalą nei UAB „Admen“. Jei grupė realiai veikia per kelias juridines įmones, vienos įmonės finansiniai rodikliai nebūtinai pilnai atspindi operacinį paveikslą.

### 6. Legal situation and past issues
Reikšmingų ilgalaikių ar sisteminių teisinių problemų atviroje paieškoje neradau. Okredo prie UAB „Admen“ nerodė registruotų skolų, o tai yra teigiamas bazinis signalas.

Vienas reikšmingesnis viešas pėdsakas - 2024-01 „Verslo žinių“ publikacija apie dingusio ir pavėluoto krovinio ginčą, žalą reputacijai Šveicarijoje ir ginčą su vežėju. Okredo šią publikaciją priskiria Admen, tačiau pilnas tekstas mokamas, todėl be papildomo teismo bylos patikrinimo nereikėtų kategoriškai teigti bylos baigties ar masto.

Rutininio žemo signalo pėdsakai yra viešųjų pirkimų ir komercinės veiklos dokumentinis fonas. Kol kas tai neatrodo kaip aukštos rizikos teisinė istorija, bet logistikos grandinės ir tarptautinio pristatymo kokybė įmonei akivaizdžiai jautri tema.

### 7. PR situation and past issues
PR profilis yra santūrus ir orientuotas į reputaciją per darbus, ne per triukšmingas kampanijas. Pagrindiniai vieši naratyvai: ilgametė patirtis, eksportas, technologinė gamyba, tvarumas ir kokybė.

Viešojoje komunikacijoje ryškus „premium klientų“ ir tarptautinių projektų akcentas. Tai gali reikšti, kad vadovybei svarbi kompetentingo, patikimo, „ne pigiausio tiekėjo“ pozicija.

Potenciali reputacinė jautrybė - pažadai apie tvarumą ir efektyvumą. Bendrovė komunikuoja 100% žaliąją elektrą, CO2 mažinimą ir perdirbtas medžiagas; tokiuose susitikimuose verta kalbėti konkrečiai, nes per daug bendri klausimai gali skambėti paviršutiniškai. Kita jautri tema - logistikos ir terminų laikymasis, turint omenyje minėtą krovinio ginčo istoriją.

### 8. SWOT
- `Stiprybės` Eksporto orientacija, reali gamybinė bazė Klaipėdoje, nuoseklus investavimas į technologijas ir darbuotojų kompetencijas, geri 2024 m. mastelio bei pelningumo rodikliai.
- `Silpnybės` Ne iki galo aiški vieša grupės/juridinių asmenų struktūra, ribotas atviras informacijos kiekis apie akcininkų ir valdymo pokyčius po „Orion“ investicijos, augę įsipareigojimai 2024 m.
- `Galimybės` Tolimesnė eksporto plėtra, didesnė aukštesnės vertės ženklinimo ir ekranų projektų dalis, LEZ aplinkoje svarbi tvarios gamybos ir operacinio efektyvumo tema.
- `Grėsmės` Tarptautinės paklausos svyravimai, projektinės gamybos maržų spaudimas, logistikos ir pristatymo kokybės rizika, reputacinė žala, jei tvarumo ar terminų pažadai neatitiktų kliento patirties.

#### Sources
- https://admen.lt/
- https://admen.lt/apie-mus/
- https://admen.lt/tvarumas/
- https://admen.lt/es-parama/
- https://admen.lt/kontaktai/
- https://okredo.com/en-lt/company/uab-admen-300860736
- https://okredo.com/lt-lt/imone/uab-admen-300860736
- https://okredo.com/en-lt/company/uab-admen-baltic-302944948
- https://rekvizitai.vz.lt/imone/admen/
- https://rekvizitai.vz.lt/imone/admen_baltic/
- https://www.oaklins.com/baltics/en/deals/106261/
- https://bsma.lt/en/member/admen/
- https://www.tenderfy.lt/lt/imone/302944948/uab_admen_baltic
- https://www.vz.lt/smulkusis-verslas/2024/02/21/ne-pelenes-istorija-is-reklamos-gamybos-300-kv-m-angare-iki-mercedes-benz-ir-hitachi-klientu
- https://www.vz.lt/rinkodara/2024/10/07/rinkodaros-sektoriaus-lyderiai-apie-sekmes-rakta-ir-fenomenalu-laikmeti-lietuvoje

session_id: 20260415_160456_33d370

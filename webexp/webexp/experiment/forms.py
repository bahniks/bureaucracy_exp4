from django import forms


questions1 = """
Jestli někdo emocionálně trpěl.
Jestli bylo s někým zacházeno jinak než s ostatními.
Jestli někdo svými činy projevoval úctu ke své vlasti.
Jestli někdo projevoval nedostatek respektu k autoritě.
Jestli se někdo choval necudně.
Jestli se někdo staral o někoho slabého nebo zranitelného.
Jestli někdo jednal nespravedlivě.
Jestli někdo udělal něco, čím zradil svou skupinu.
Jestli někdo jednal v souladu s tradicemi společnosti.
Jestli někdo udělal něco nechutného.
Jestli byl někdo krutý.
Jestli byla někomu upřena jeho práva.
Jestli někdo projevil nedostatek loajality.
Jestli něčí činy způsobily zmatek nebo narušení pořádku.
Jestli někdo jednal tak, jak by to Bůh schvaloval.
""".strip().split("\n")
answers1 = [(1, "zcela nepodstatné"), 
            (2, "nepříliš podstatné"), 
            (3, "mírně podstatné"), 
            (4, "celkem podstatné"), 
            (5, "velmi podstatné"), 
            (6, "obzvlášť podstatné")]

mfq1_instructions = "Při posuzování, zda je něco správné nebo špatné, berou lidé v potaz různé kritéria. Do jaké míry jsou pro Vás následující skutečnosti důležité, když hodnotíte, zda bylo něco správné nebo špatné?"

questions2 = """
Soucit s těmi, kdo trpí, je nejdůležitější ctnost.
Když zákonodárci tvoří zákony, nejdůležitějším principem by mělo být zajištění spravedlivého zacházení pro všechny.
Jsem hrdý/ hrdá na historii své země.
Respekt k autoritě by se měly naučit všechny děti.
Lidé by neměli dělat nechutné věci, ani když jimi nikomu neškodí.
Je lepší dělat dobro než zlo.
Jednou z nejhorších věcí, které může člověk udělat, je zranit bezbranné zvíře.
Spravedlnost je nejdůležitějším předpokladem společnosti.
Lidé by měli být loajální ke členům své rodiny, i když udělali něco špatného.
Muži a ženy mají hrát ve společnosti odlišné role.
Některé činy považuji za špatné proto, že jsou nepřirozené.
Zabít lidskou bytost nemůže být nikdy správné.
Myslím si, že je nemorální, že děti z bohatých rodin zdědí mnoho peněz, zatímco děti z chudých rodin nezdědí nic.
Je důležitější být týmovým hráčem, než projevovat sebe sama.
Kdybych byl(a) v armádě a nesouhlasil(a) bych s rozkazy nadřízeného, stejně bych je uposlechl(a), protože to je má povinnost.
Sexuální zdrženlivost je důležitá a hodnotná ctnost.
Když lidé usilují o společný cíl, měli by mít stejný podíl na výsledné odměně, i když někteří pracovali usilovněji a přispěli víc než jiní.
Všichni členové společnosti by měli ideálně skončit se zhruba stejným množstvím peněz.
Spravedlnost pro mě znamená, že k lidem by se mělo přistupovat stejně, bez ohledu na jejich odlišnosti.
Při rozdělování bonusu je podle mě spravedlivé, aby všichni dostali stejný podíl.
Myslím si, že některé skupiny lidí čelí mnohem větším překážkám v dosažení úspěchu než jiné a k překonání těchto překážek je nezbytné, aby se společnost více snažila o jejich odstranění a poskytnutí dodatečné podpory. 
Spravedlnost pro mě znamená, že každý dostane, co potřebuje, aby uspěl, i když to znamená, že někteří lidé dostanou víc než jiní, protože od začátku čelí větším překážkám. 
Obecně by lidé, kteří pracují víc, měli být placeni víc než jejich kolegové na stejné úrovni, i když to povede k nerovným výsledkům.
Když děti soupeří ve sportovních disciplínách, myslím si, že je důležité ocenit vítěze za jejich úspěchy.
Při rozdělování bonusu je podle mě spravedlivé, aby každý dostal podíl dle svých zásluh: lidé, co přispěli nejvíce, by měli dostat největší odměnu.
Spravedlnost pro mě znamená, že by lidé měli být odměňováni podle velikosti svého přínosu.
Opravdu mě rozčiluje, když vidím jak někdo nedělá svůj spravedlivý díl práce.
Když pracuji s ostatními, vždy mám přehled o tom, kdo přispěl víc a kdo méně.
""".strip().split("\n")

answers2 = [(1, "zcela nesouhlasím"), 
            (2, "nesouhlasím"), 
            (3, "spíše nesouhlasím"), 
            (4, "spíše souhlasím"), 
            (5, "souhlasím"), 
            (6, "silně souhlasím")]

mfq2_instructions = """<p>V této části je uvedena řada výroků.</p>
<p>Přečtěte si, prosím, postupně každý výrok a vždy se rozhodněte, jak moc s ním souhlasíte nebo nesouhlasíte.</p>"""


questions3 = """
Prováděný úkol byl náročný.
Prováděný úkol byl zajímavý.
Prováděný úkol byl nudný.
Prováděný úkol byl únavný.
Prováděný úkol byl dlouhý.
Odměna za každé zatřídění byla dostatečná.
Odměna za každé zatřídění byla spravedlivá.
Odměna za každé zatřídění byla v porovnání s odměnou ostatních nespravedlivá.
Odměna za každé zatřídění byla nízká.
S odměnou za každé zatřídění jsem byl(a) spokojený/-á.
Se svým výkonem v úloze jsem byl(a) spokojený/-á.
Obrazce se pohybovaly příliš pomalu.
Obrazce se pohybovaly příliš rychle.
Částky nabízené za zatřídění dle TVARU byly obvykle vysoké.
Částky nabízené za zatřídění dle TVARU byly obvykle nízké.
Ztráta pro charitu za špatné zatřídění dle BARVY byla vysoká. 
Ztráta pro charitu za špatné zatřídění dle BARVY motivovala ke správnému třídění.
Počáteční body přidělené charitě byly nízké.
Počáteční body přidělené charitě byly dostatečné.
Výběr charitativní organizace byl příliš malý.
Výběr charitativní organizace byl dostatečný.
Instrukce k úloze byly srozumitelné.
Instrukce k úloze byly komplikované.
Instrukce k úloze byly dlouhé.
""".strip().split("\n")

perception_instructions = "<p>Na uvedené škále uveďte, nakolik souhlasíte s následujícími tvrzeními.</p>"


class MFQ1(forms.Form):
    for n, question in enumerate(questions1):
        locals()["question" + str(n)] = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"class": "horizontal_buttons"}), choices = answers1, label = question, error_messages={'required': 'Tato otázka je vyžadována.'})


class MFQ2(forms.Form):
    for n, question in enumerate(questions2):
        locals()["question" + str(n + len(questions1))] = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"class": "horizontal_buttons"}), choices = answers2, label = question, error_messages={'required': 'Tato otázka je vyžadována.'})


class Perception(forms.Form):
    for n, question in enumerate(questions3):
        locals()["question" + str(n + len(questions1) + len(questions2))] = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"class": "horizontal_buttons"}), choices = answers2, label = question, error_messages={'required': 'Tato otázka je vyžadována.'})
from django import forms


questions1 = """
Jestli někdo citově strádal
Jestli se s některými lidmi zacházelo jinak, než s ostatními
Jestli někdo svými činy projevoval lásku ke své zemi
Jestli někdo projevoval nedostatek respektu k autoritě
Jestli někdo porušil standardy počestnosti a slušnosti
Jestli byl někdo dobrý v matematice
Jestli se někdo staral o někoho slabého nebo zranitelného
Jestli někdo jednal nespravedlivě
Jestli někdo udělal něco, čím zradil svou skupinu
Jestli někdo jednal v souladu s tradicemi společnosti
Jestli někdo udělal něco nechutného
Jestli byl někdo krutý
Jestli byla někomu upřena jeho práva
Jestli někdo projevil nedostatek loajality
Jestli něčí činy způsobily zmatek nebo nepokoj
Jestli někdo jednal způsobem, který by Bůh schvaloval
""".strip().split("\n")
answers1 = [(1, "zcela nepodstatné"), 
            (2, "nepříliš podstatné"), 
            (3, "mírně podstatné"), 
            (4, "celkem podstatné"), 
            (5, "velmi podstatné"), 
            (6, "obzvlášť podstatné")]

questions2 = """
Soucit s těmi, kdo trpí, je nejdůležitější ctnost.
Když zákonodárci tvoří zákony, nejdůležitějším principem by mělo být zajištění spravedlivého zacházení pro všechny.
Jsem hrdý/ hrdá na historii své země.
Respekt k autoritě by se měly naučit všechny děti.
Lidé by neměli dělat nechutné věci, i když tím nikomu neškodí.
Je lepší dělat dobro než zlo.
Jednou z nejhorších věcí, které může člověk udělat, je zranit bezbranné zvíře.
Spravedlnost je nejdůležitějším základním kamenem společnosti.
Lidé by měli být loajální ke členům své rodiny, i když udělali něco špatného.
Muži a ženy mají hrát ve společnosti odlišné role.
Některé činy bych nazval(a) špatnými na základě toho, že jsou nepřirozené.
Zabití lidské bytosti nemůže být nikdy správné.
Myslím si, že je morálně špatné, že děti z bohatých rodin zdědí mnoho peněz, zatímco děti z chudých rodin nezdědí nic.
Je důležitější být týmovým hráčem, než projevovat sebe sama.
Kdybych byl(a) v armádě a nesouhlasil(a) bych s rozkazy nadřízeného, stejně bych je uposlechl(a), protože to je má povinnost.
Cudnost je důležitá a hodnotná ctnost.
""".strip().split("\n")

answers2 = [(1, "zcela nesouhlasím"), 
            (2, "docela nesouhlasím"), 
            (3, "trochu nesouhlasím"), 
            (4, "trochu souhlasím"), 
            (5, "docela souhlasím"), 
            (6, "silně souhlasím")]


class MFQ1(forms.Form):
    for n, question in enumerate(questions1):
        locals()["question" + str(n)] = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"class": "horizontal_buttons"}), choices = answers1, label = question, 
                                                          error_messages={'required': 'Tato otázka je vyžadována.'})


class MFQ2(forms.Form):
    for n, question in enumerate(questions2):
        locals()["question" + str(n + len(questions1))] = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"class": "horizontal_buttons"}), choices = answers2, label = question,
                                                                            error_messages={'required': 'Tato otázka je vyžadována.'})
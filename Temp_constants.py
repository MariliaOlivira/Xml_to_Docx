DIR = '/home/francisco/Desktop/planilhas_escolas/modelos_planilhas'

anyconv =  'AnyConv.com__'
dirTempl = f'{DIR}/%s'
ppTempl = f'{anyconv}pesquisa_de_preco_%s.docx'
listConc = ['samel', 'atuante', 'enoque']

DICT_P_P = {name : dirTempl % (ppTempl % name) for name in listConc}
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class LancheApp(App):

    def build(self):
        root = FloatLayout()

        layout = GridLayout(cols=2, spacing=10, size_hint=(None, None), size=(400, 300), pos_hint={'x': .3, 'y': .3})
        layout.bind(minimum_height=layout.setter('height'))

        label_pessoa = Label(text="Nome da Pessoa:", size_hint=(None, None), size=(150, 30), valign='middle')
        layout.add_widget(label_pessoa)
        self.entry_pessoa = TextInput()
        layout.add_widget(self.entry_pessoa)

        label_paes = Label(text="Quantidade de Pães Consumidos:", size_hint=(None, None), size=(150, 30), valign='middle')
        layout.add_widget(label_paes)
        self.entry_paes = TextInput()
        layout.add_widget(self.entry_paes)

        label_valor_total_paes = Label(text="Valor Total dos Pães (R$):", size_hint=(None, None), size=(150, 30), valign='middle')
        layout.add_widget(label_valor_total_paes)
        self.entry_valor_total_paes = TextInput()
        layout.add_widget(self.entry_valor_total_paes)

        label_valor_total_refrigerantes = Label(text="Valor Total dos Refrigerantes (R$):", size_hint=(None, None), size=(150, 30), valign='middle')
        layout.add_widget(label_valor_total_refrigerantes)
        self.entry_valor_total_refrigerantes = TextInput()
        layout.add_widget(self.entry_valor_total_refrigerantes)

        label_pix = Label(text="PIX da Pessoa:", size_hint=(None, None), size=(150, 30), valign='middle')
        layout.add_widget(label_pix)
        self.entry_pix = TextInput()
        layout.add_widget(self.entry_pix)

        btn_adicionar = Button(text="Adicionar Consumo", size_hint=(None, None), size=(150, 30))
        btn_adicionar.bind(on_press=self.adicionar_consumo)
        layout.add_widget(btn_adicionar)

        btn_calcular = Button(text="Calcular Valor Total", size_hint=(None, None), size=(150, 30))
        btn_calcular.bind(on_press=self.calcular_valor_total)
        layout.add_widget(btn_calcular)

        # Inicializar a lista para armazenar os consumos
        self.consumos = []

        root.add_widget(layout)

        return root

    def adicionar_consumo(self, instance):
        pessoa = self.entry_pessoa.text
        paes_consumidos = self.entry_paes.text

        if not pessoa or not paes_consumidos:
            self.mostrar_erro("Por favor, preencha todos os campos.")
            return

        try:
            paes_consumidos = int(paes_consumidos)
        except ValueError:
            self.mostrar_erro("Por favor, insira uma quantidade válida de pães.")
            return

        # Armazenando os dados do consumo na lista
        self.consumos.append({
            'Nome da Pessoa': pessoa,
            'Quantidade de Pães Consumidos': paes_consumidos,
        })

        print("Consumo adicionado com sucesso.")

        # Limpar os campos de entrada após adicionar o consumo
        self.entry_pessoa.text = ''
        self.entry_paes.text = ''

    def calcular_valor_total(self, instance):
        valor_total_paes = self.entry_valor_total_paes.text
        valor_total_refrigerantes = self.entry_valor_total_refrigerantes.text

        if not valor_total_paes or not valor_total_refrigerantes:
            self.mostrar_erro("Por favor, preencha os valores dos pães e refrigerantes.")
            return

        try:
            valor_total_paes = float(valor_total_paes)
            valor_total_refrigerantes = float(valor_total_refrigerantes)
        except ValueError:
            self.mostrar_erro("Por favor, insira valores numéricos válidos.")
            return

        if valor_total_paes == 0:
            self.mostrar_erro("O valor total dos pães não pode ser zero.")
            return

        total_pessoas = len(self.consumos)
        total_paes = sum(consumo['Quantidade de Pães Consumidos'] for consumo in self.consumos)

        valor_por_pao = valor_total_paes / total_paes
        valor_por_refrigerante = valor_total_refrigerantes / total_pessoas

        for consumo in self.consumos:
            valor_pessoa = consumo['Quantidade de Pães Consumidos'] * valor_por_pao
            print(f"{consumo['Nome da Pessoa']}: Pães: R${valor_pessoa:.2f}, Refrigerantes: R${valor_por_refrigerante:.2f}")

    def mostrar_erro(self, mensagem):
        print("Erro:", mensagem)

if __name__ == '__main__':
    LancheApp().run()

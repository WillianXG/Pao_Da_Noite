from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from datetime import datetime

class LancheApp(App):

    def build(self):
        root = FloatLayout()

        layout = GridLayout(cols=2, spacing=10, size_hint=(None, None), size=(400, 200), pos_hint={'x': .3, 'y': .3})
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

        root.add_widget(layout)

        return root

    def adicionar_consumo(self, instance):
        pessoa = self.entry_pessoa.text
        paes_consumidos = self.entry_paes.text
        valor_total_paes = self.entry_valor_total_paes.text
        valor_total_refrigerantes = self.entry_valor_total_refrigerantes.text
        pix = self.entry_pix.text

        print("Dados inseridos:")
        print("Nome da Pessoa:", pessoa)
        print("Quantidade de Pães Consumidos:", paes_consumidos)
        print("Valor Total dos Pães (R$):", valor_total_paes)
        print("Valor Total dos Refrigerantes (R$):", valor_total_refrigerantes)
        print("PIX da Pessoa:", pix)

    def calcular_valor_total(self, instance):
        print("Botão 'Calcular Valor Total' pressionado.")

if __name__ == '__main__':
    LancheApp().run()

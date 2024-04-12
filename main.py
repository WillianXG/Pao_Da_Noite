from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from datetime import datetime

# Lista para armazenar os consumos
consumo_paes = []

class LancheApp(App):

    def build(self):
        root = FloatLayout()

        layout = GridLayout(cols=2, spacing=10, size_hint=(None, None), size=(400, 400), pos_hint={'x': .3, 'y': .2})
        layout.bind(minimum_height=layout.setter('height'))

        label_pessoa = Label(text="Nome da Pessoa:", size_hint=(None, None), size=(150, dp(30)), valign='middle')
        layout.add_widget(label_pessoa)
        self.entry_pessoa = TextInput()
        layout.add_widget(self.entry_pessoa)

        label_paes = Label(text="Quantidade de Pães Consumidos:", size_hint=(None, None), size=(150, dp(30)), valign='middle')
        layout.add_widget(label_paes)
        self.entry_paes = TextInput()
        layout.add_widget(self.entry_paes)

        label_valor_total_paes = Label(text="Valor Total dos Pães (R$):", size_hint=(None, None), size=(150, dp(30)), valign='middle')
        layout.add_widget(label_valor_total_paes)
        self.entry_valor_total_paes = TextInput()
        layout.add_widget(self.entry_valor_total_paes)

        label_valor_total_refrigerantes = Label(text="Valor Total dos Refrigerantes (R$):", size_hint=(None, None), size=(150, dp(30)), valign='middle')
        layout.add_widget(label_valor_total_refrigerantes)
        self.entry_valor_total_refrigerantes = TextInput()
        layout.add_widget(self.entry_valor_total_refrigerantes)

        label_pix = Label(text="PIX da Pessoa:", size_hint=(None, None), size=(150, dp(30)), valign='middle')
        layout.add_widget(label_pix)
        self.entry_pix = TextInput()
        layout.add_widget(self.entry_pix)

        btn_adicionar = Button(text="Adicionar Consumo", size_hint=(None, None), size=(150, dp(30)))
        btn_adicionar.bind(on_press=self.adicionar_consumo)
        layout.add_widget(btn_adicionar)

        btn_calcular = Button(text="Calcular Valor Total", size_hint=(None, None), size=(150, dp(30)))
        btn_calcular.bind(on_press=self.calcular_valor_total)
        layout.add_widget(btn_calcular)

        btn_visualizar_participantes = Button(text="Visualizar Participantes", size_hint=(None, None), size=(300, dp(30)))
        btn_visualizar_participantes.bind(on_press=self.visualizar_participantes)
        layout.add_widget(btn_visualizar_participantes)

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
        consumo_paes.append((pessoa, paes_consumidos))

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

        total_pessoas = len(consumo_paes)
        total_paes = sum(qtd_paes for pessoa, qtd_paes in consumo_paes)

        valor_por_pao = valor_total_paes / total_paes
        valor_por_refrigerante = valor_total_refrigerantes / total_pessoas

        resultado = "Valor a pagar por pessoa:\n"
        for pessoa, qtd_paes in consumo_paes:
            valor_pessoa = qtd_paes * valor_por_pao + valor_por_refrigerante
            resultado += f"R$ {valor_pessoa:.2f} : {pessoa}\n"

        resultado += f"\nPIX: {self.entry_pix.text}\n"
        resultado += f"Data: {datetime.now().strftime('%d/%m/%Y')}\n"

        popup = Popup(title='Resultados', content=Label(text=resultado), size_hint=(None, None), size=(400, 400))
        popup.open()

    def visualizar_participantes(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10, padding=0)
        for pessoa, qtd_paes in consumo_paes:
            box_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=dp(40))

            label_pessoa = Label(text=f"{pessoa}", size_hint=(None, None), width=150, halign='left')
            box_layout.add_widget(label_pessoa)

            label_qtd_paes = Label(text=f"Pães: {qtd_paes}", size_hint=(None, None), width=100, halign='left')
            box_layout.add_widget(label_qtd_paes)

            btn_editar_paes = Button(text="Editar", size_hint=(None, None), size=(80, dp(30)))
            btn_editar_paes.bind(on_press=lambda _, pessoa=pessoa: self.editar_quantidade_paes(pessoa))
            box_layout.add_widget(btn_editar_paes)

            btn_excluir_pessoa = Button(text="Excluir", size_hint=(None, None), size=(80, dp(30)))
            btn_excluir_pessoa.bind(on_press=lambda _, pessoa=pessoa: self.excluir_participante(pessoa))
            box_layout.add_widget(btn_excluir_pessoa)

            content.add_widget(box_layout)

        popup = Popup(title='Participantes', content=content, size_hint=(None, None), size=(550, 500))
        popup.open()


    def editar_quantidade_paes(self, pessoa):
        # Encontrar a pessoa na lista de consumo_paes
        for index, (p, _) in enumerate(consumo_paes):
            if p == pessoa:
                content = BoxLayout(orientation='vertical', spacing=10, padding=10)
                content.add_widget(Label(text=f"Pessoa: {pessoa}"))

                entry_qtd_paes = TextInput(text=str(consumo_paes[index][1]), multiline=False)
                content.add_widget(entry_qtd_paes)

                btn_salvar = Button(text="Salvar", size_hint=(None, None), size=(100, dp(30)))
                btn_salvar.bind(on_press=lambda _: self.salvar_edicao_quantidade_paes(index, entry_qtd_paes.text))
                content.add_widget(btn_salvar)

                popup = Popup(title='Editar Quantidade de Pães', content=content, size_hint=(None, None), size=(300, 200))
                popup.open()
                break

    def salvar_edicao_quantidade_paes(self, index, nova_quantidade):
        try:
            nova_quantidade = int(nova_quantidade)
        except ValueError:
            self.mostrar_erro("Por favor, insira uma quantidade válida de pães.")
            return

        consumo_paes[index] = (consumo_paes[index][0], nova_quantidade)
        popup = Popup(title='Sucesso', content=Label(text="Quantidade de pães editada com sucesso."), size_hint=(None, None), size=(300, 150))
        popup.open()

    def excluir_participante(self, pessoa):
        for index, (p, _) in enumerate(consumo_paes):
            if p == pessoa:
                del consumo_paes[index]
                popup = Popup(title='Sucesso', content=Label(text="Participante excluído com sucesso."), size_hint=(None, None), size=(300, 150))
                popup.open()
                break

    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    LancheApp().run()

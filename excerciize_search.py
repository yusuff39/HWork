import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

class InteractivePlot:
    def __init__(self):
        # Figür ve eksen oluştur
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.plot_data(self.data)

        # Arama metni ve butonları oluştur
        self.text_box_ax = plt.axes([0.1, 0.05, 0.2, 0.075])
        self.search_button_ax = plt.axes([0.35, 0.05, 0.1, 0.075])
        
        self.text_box = TextBox(self.text_box_ax, 'Arama:')
        self.search_button = Button(self.search_button_ax, 'Ara')
        self.search_button.on_clicked(self.perform_search)

        plt.show()

    def plot_data(self, data):
        self.ax.clear()
        self.ax.plot(data, 'o-')
        self.ax.set_title('Veri Grafiği')
        self.ax.set_xlabel('X Ekseni')
        self.ax.set_ylabel('Y Ekseni')

    def perform_search(self, event):
        search_value = self.text_box.text
        if search_value:
            try:
                search_value = int(search_value)
                if search_value in self.data:
                    index = self.data.index(search_value)
                    self.highlight_point(index)
                else:
                    print("Değer bulunamadı!")
            except ValueError:
                print("Geçersiz arama değeri!")
        else:
            print("Arama değeri girilmedi!")

    def highlight_point(self, index):
        self.plot_data(self.data)
        self.ax.plot(index, self.data[index], 'ro', markersize=10)  # Aranan noktayı kırmızı ile işaretle
        self.fig.canvas.draw()

# Uygulamayı başlat
InteractivePlot()

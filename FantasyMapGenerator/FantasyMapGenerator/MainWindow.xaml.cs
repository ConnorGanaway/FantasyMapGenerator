using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;
using System.Diagnostics;
using IronPython.Hosting;

namespace FantasyMapGenerator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            
            if (MapView.Visibility == Visibility.Hidden)
            {
                MapView.Visibility = Visibility.Visible;
            }
            else
            {
                MapView.Visibility = Visibility.Hidden;
            }
            
        }

        //Size Input
        private void TextBox_TextChanged_1(object sender, TextChangedEventArgs e)
        {

        }

        //Seed Input
        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        //Night Time Mode
        private void DarkMode_Checked(object sender, RoutedEventArgs e)
        {

        }

        //Generate Paths
        private void Paths_Checked(object sender, RoutedEventArgs e)
        {

        }

        //TBD Generation Option
        private void CheckBox_Checked_3(object sender, RoutedEventArgs e)
        {
            scale.Value = 100;
            octaves.Value = 7;  
            persistence.Value = 0.5;
            lacunarity.Value = 1.5;
        }

        //TBD Generation Option
        private void CheckBox_Checked_4(object sender, RoutedEventArgs e)
        {

        }

        //Slider for scale
        private void scale_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            
        }

        //Slider for octaves
        private void octaves_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        //Slider for persistence
        private void persistence_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        //Slider for lacunarity
        private void lacunarity_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }
    }
}

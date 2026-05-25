import gradio as gr
import sys
sys.path.append('/Users/ym31/Desktop/laptop prediction/server')
import util

util.load_artifacts()

def predict(company, inches, screen, cpu, ram, memory, gpu, weight):
    return util.estimated_price(company, inches, screen, cpu, ram, memory, gpu, weight)


demo = gr.Interface(
    fn = predict,
    inputs=[
        gr.Dropdown(choices= util.get_full_names()['company'], label='COMPANY'),
        gr.Number(label = 'INCHES'),
        
        gr.Dropdown(choices = util.get_full_names()['screenresolution'], label = 'SCREEN'),
        gr.Dropdown(choices=util.get_full_names()['cpu'], label='CPU'),
        gr.Number(label ='RAM (GB)'),
        gr.Dropdown(choices=util.get_full_names()['memory'], label='Memory'),
        gr.Dropdown(choices= util.get_full_names()['gpu'], label='GPU'),
        gr.Dropdown(label = 'WEIGHT(KG)')
    ],

    outputs = gr.Number(label = "ESTIMATED LAPTOP PRICE IN EUROS "),
)

if __name__ =='__main__':

    demo.launch(share=True)
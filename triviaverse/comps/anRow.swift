//
//  anRow.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct anRow: View {
    @EnvironmentObject  var triviaManager: TriviaManager
    var answer: Answer
    @State private var isSelected = false
    
    var green = Color(hue: 0.437, saturation: 0.711,
                      brightness: 0.711)
    var red = Color(red: 0.71, green: 0.094, blue: 0.1)
    
    var body: some View {
        HStack(spacing: 20){
            Image(systemName: "circle.fill").font(.caption)
            
            Text(answer.text).bold()
            
            if isSelected {
                Spacer()
                
                Image(systemName: answer.isCorrect ? "checkmark.circle.fill": "x.circle").foregroundColor(answer.isCorrect ? green : red)
            }
            
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
                .foregroundColor(triviaManager.answerSelected ? (isSelected ? Color("AccentColor") : .gray) : Color("AccentColor"))
                .background(.white)
                .cornerRadius(10)
                .shadow(color: isSelected ? answer.isCorrect ? green : red : .gray, radius: 5, x: 0.5, y: 0.5)
                .onTapGesture {
                    if !triviaManager.answerSelected {
                        isSelected = true
                        triviaManager.chooseAnswer(answer: answer)
            }
        
        }
    }
}

struct anRow_Previews: PreviewProvider {
    static var previews: some View {
        anRow(answer: Answer(text: "19", isCorrect: false)).environmentObject(TriviaManager())
    }
}

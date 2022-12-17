//
//  progV.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct progV: View {
    var progress: CGFloat
    
    var body: some View {
        ZStack(alignment: .leading){
            Rectangle().frame(maxWidth: 350, maxHeight: 4).foregroundColor(Color(hue: 1.0, saturation: 0.0, brightness: 0.56, opacity: 0.33)).cornerRadius(10)
            
            Rectangle().frame(width: progress, height: 4).foregroundColor(Color("AccentColor")).cornerRadius(10)
        }
    }
}

struct progV_Previews: PreviewProvider {
    static var previews: some View {
        progV(progress: 75)
    }
}
